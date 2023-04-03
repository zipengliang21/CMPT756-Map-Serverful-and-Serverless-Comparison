from src.navigation.database.entity import EdgeAttributes
from src.navigation.database.entity import AdjacentEdges
from src.navigation.database.navigation import AddEdges
from src.navigation.database.navigation import DeleteEdges
from src.navigation.database.navigation import findEdges
from src.mutation.proto_py.mutation_pb2 import MutationRequests


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
        map = requests

        for request in map.requests:
            distance = EdgeAttributes(request.write_edge.distance)

            node_a_id = request.write_edge.node_a.id
            node_b_id = request.write_edge.node_b.id

            edgeAttributes_a = {node_a_id: distance}
            edgeAttributes_b = {node_b_id: distance}

            edges_a = AdjacentEdges(node_a_id, edgeAttributes_b)
            edges_b = AdjacentEdges(node_b_id, edgeAttributes_a)

            AddEdges(edges_a, self.db_conn)
            AddEdges(edges_b, self.db_conn)
