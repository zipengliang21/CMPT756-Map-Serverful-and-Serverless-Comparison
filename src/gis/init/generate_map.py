from src.rndgraph.node import Node
from src.rndgraph.node import GenerateNodes
from src.rndgraph.edge import GenerateMstEdges
from src.gis.proto_py.mutation_pb2 import Node as ProtoNode
from src.gis.proto_py.mutation_pb2 import WriteUndirectedEdgeRequest
from src.gis.proto_py.mutation_pb2 import MutationRequest
from src.gis.proto_py.mutation_pb2 import MutationRequests

_NODE_SIZE = 100000
_RADIUS = 100


def _ToProtoNode(node: Node) -> ProtoNode:
    return ProtoNode(id=node.id,
                     location=ProtoNode.Location(
                         x=node.location.x,
                         y=node.location.y),
                     importance=node.importance)


def GenerateInitialMap() -> MutationRequests:
    """Generates pseudo-random inital map. Note, this function idempotent.

    Returns:
        MutationRequests: The mutations needed to constructs the initial map.
    """
    nodes = GenerateNodes(node_count=_NODE_SIZE, radius=_RADIUS)
    edges = GenerateMstEdges(nodes=nodes)

    requests = list()

    for edge in edges:
        node_a = _ToProtoNode(node=edge.node_a)
        node_b = _ToProtoNode(node=edge.node_b)

        write_edge_request = WriteUndirectedEdgeRequest(
            node_a=node_a,
            node_b=node_b,
            distance=edge.euclidean_distance)
        request = MutationRequest(write_edge=write_edge_request)

        requests.append(request)

    return MutationRequests(requests=requests)
