from typing import Dict
from typing import List
from typing import Set
from typing import Tuple


from src.gis.database.entity import Geolocation
from src.gis.database.entity import Topology
from src.gis.database.update import WriteGeolocations
from src.gis.database.update import WriteTopology
from src.gis.database.update import DeleteTopology
from src.mutation.proto_py.mutation_pb2 import MutationRequests
from src.mutation.proto_py.mutation_pb2 import MutationRequest
from src.mutation.proto_py.mutation_pb2 import WriteUndirectedEdgeRequest
from src.mutation.proto_py.mutation_pb2 import Node


def _ToGeolocation(node: Node) -> Geolocation:
    return Geolocation(id=node.id,
                       x=node.location.x,
                       y=node.location.y,
                       importance=node.importance)


def CollectGeolocations(
        requests: List[MutationRequest]) -> Dict[int, Geolocation]:
    """Internal function.
    """
    result = dict()

    for request in requests:
        if request.write_edge is None:
            continue

        loc_a = _ToGeolocation(node=request.write_edge.node_a)
        loc_b = _ToGeolocation(node=request.write_edge.node_b)

        result[loc_a.id] = loc_a
        result[loc_b.id] = loc_b

    return result


class TopologyCollection:
    """Internal class
    """

    def __init__(self) -> None:
        self.additions: Dict[Tuple[int, int], Topology] = dict()
        self.deletions: Set[Tuple[int, int]] = set()


def _ToTopology(
        write_edge: WriteUndirectedEdgeRequest) -> Tuple[Topology, Topology]:
    return (
        Topology(loc1_id=write_edge.node_a.id,
                 loc2_id=write_edge.node_b.id,
                 distance=write_edge.distance),
        Topology(loc1_id=write_edge.node_b.id,
                 loc2_id=write_edge.node_a.id,
                 distance=write_edge.distance)
    )


def CollectTopology(
        requests: List[MutationRequest]) -> TopologyCollection:
    """Internal function.
    """
    result = TopologyCollection()

    for request in requests:
        if request.WhichOneof("request") == "write_edge":
            topology1, topology2 = _ToTopology(write_edge=request.write_edge)

            result.additions[(topology1.loc1_id, topology1.loc2_id)] = \
                topology1
            result.additions[(topology2.loc1_id, topology2.loc2_id)] = \
                topology2
        elif request.WhichOneof("request") == "delete_edge":
            connection1 = (request.delete_edge.node_a_id,
                           request.delete_edge.node_b_id)
            connection2 = (request.delete_edge.node_b_id,
                           request.delete_edge.node_a_id)

            if (connection1 in result.additions) or \
                    (connection2 in result.additions):
                del result.additions[connection1]
                del result.additions[connection2]
            else:
                result.deletions.add(connection1)
                result.deletions.add(connection2)
        else:
            assert False

    return result


class MutationWriter:
    """_summary_
    """

    def __init__(self, db_conn) -> None:
        """_summary_

        Args:
            db_conn (_type_): _description_
        """
        self.db_conn = db_conn

    def Materialize(self, requests: MutationRequests) -> None:
        """_summary_

        Args:
            requests (MutationRequests): _description_
        """
        locations = CollectGeolocations(requests=requests.requests)
        WriteGeolocations(locations=locations, db_conn=self.db_conn)

        topology = CollectTopology(requests=requests.requests)
        WriteTopology(topology=topology.additions, db_conn=self.db_conn)
        DeleteTopology(links=topology.deletions, db_conn=self.db_conn)
