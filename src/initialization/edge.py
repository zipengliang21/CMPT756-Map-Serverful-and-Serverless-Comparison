
import numpy as np
from typing import List
from typing import Set

from src.initialization.node import Node
from src.initialization.node import EuclideanDistance


class UndirectedEdge:
    """Represents an undirected edge in a graph.
    """

    def __init__(self,
                 node_a: Node,
                 node_b: Node):
        assert node_a is not None
        assert node_b is not None

        self.node_a = node_a
        self.node_b = node_b
        self.euclidean_distance = EuclideanDistance(a=node_a, b=node_b)

    def __repr__(self):
        return f"UndirectedEdge[{self.node_a},{self.node_b},"\
            f"{self.euclidean_distance}]"


def _SelectRandomTargets(nodes: List[Node], num_targets: int) -> Set[int]:
    assert len(nodes) >= num_targets

    targets = set()

    while len(targets) < num_targets:
        target = np.random.randint(low=0, high=len(nodes), size=1)
        targets.add(target[0])

    return targets


class _GraphComponents:
    def __init__(self, nodes: List[Node]) -> None:
        self.parent_of = dict()

        for node in nodes:
            self.parent_of[node.id] = node.id

    def _RootOf(self, node: int) -> int:
        parent = self.parent_of[node]
        if parent == node:
            return node

        root = self._RootOf(parent)
        self.parent_of[node] = root

        return root

    def ComponentIdOf(self, node: Node) -> bool:
        return self._RootOf(node=node.id)

    def Connect(self, component_a: int, component_b: int) -> None:
        self.parent_of[component_b] = component_a


def Mst(nodes: List[Node],
        edges: List[UndirectedEdge]) -> List[UndirectedEdge]:
    """Internal function exposed for testing purposes.
    """
    result_edges = list()
    result_components = _GraphComponents(nodes=nodes)

    shortest_edges = sorted(edges, key=lambda e: -e.euclidean_distance)

    while len(shortest_edges) > 0:
        candid_edge = shortest_edges.pop()

        component_a = result_components.ComponentIdOf(candid_edge.node_a)
        component_b = result_components.ComponentIdOf(candid_edge.node_b)
        if component_a == component_b:
            continue

        result_edges.append(candid_edge)
        result_components.Connect(component_a, component_b)

    return result_edges


def GenerateRandomEdges(nodes: List[Node],
                        out_degree: int) -> List[UndirectedEdge]:
    """It generates a random graph by connecting each node to out_degree
    number of other nodes.

    Args:
        nodes (List[Node]): The list of nodes that are in the graph.
        out_degree (int): How many nodes to connect against for every node.

    Returns:
        List[UndirectedEdge]: The generated list of undirected edges in the
            graph.
    """
    assert len(nodes) > out_degree
    nodes = nodes.copy()
    np.random.seed(seed=13)

    result_edges = list()
    while len(nodes) > out_degree:
        source_node = nodes.pop()

        targets = _SelectRandomTargets(nodes=nodes, num_targets=out_degree)
        for target in targets:
            target_node = nodes[target]
            edge = UndirectedEdge(node_a=source_node, node_b=target_node)

            result_edges.append(edge)

    return result_edges


def GenerateMstEdges(nodes: List[Node]) -> List[UndirectedEdge]:
    """It generates a random graph by initially sparsely connecting the nodes,
    then it finds the minimum spanning tree from the graph.

    Args:
        nodes (List[Node]): The list of nodes that are in the graph.

    Returns:
        List[UndirectedEdge]: The generated list of undirected edges in the
            graph.
    """
    DEG = min(len(nodes) - 1, 2)
    edges = GenerateRandomEdges(nodes=nodes, out_degree=DEG)
    return Mst(nodes=nodes, edges=edges)
