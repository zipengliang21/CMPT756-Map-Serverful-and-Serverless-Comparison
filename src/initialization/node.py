import math
import numpy as np
from typing import List


class Location:
    """Represents a 2D location in Cartesian coordindate system.
    """

    def __init__(self, x: float, y: float) -> None:
        """Constructs a 2D location.

        Args:
            x (float): _description_
            y (float): _description_
        """
        self.x = x
        self.y = y


class Node:
    """Represents a graph node.
    """

    def __init__(self,
                 id: int,
                 location: Location):
        """Construct a graph node

        Args:
            id (int): Unique identifier in a graph.
            location (Location): a 2D location.
        """
        self.id = id
        self.location = location

    def __repr__(self):
        return f"Node {self.id}"


def EuclideanDistance(a: Node, b: Node) -> float:
    """Calculates the Euclidean distance between the two specified nodes.
    """
    dx = a.location.x - b.location.x
    dy = a.location.y - b.location.y
    return math.sqrt(dx*dx + dy*dy)


def GenerateNodes(node_count: int, radius: float) -> List[Node]:
    """Generates node_count number of nodes whose locations are pseudo-randomly
    scattered in a disk of radius r. Note, this function is idempotent.

    Args:
        node_count (int): The number of nodes to generate.
        radius (float): The maximum radius a node can be placed from the
            origin.

    Returns:
        List[Node]: A list of pseudo-randomly generated nodes.
    """
    np.random.seed(seed=13)
    alpha = np.random.uniform(low=0, high=2*np.pi, size=node_count)
    r = radius*np.sqrt(np.random.uniform(low=0, high=1, size=node_count))

    xs = r*np.cos(alpha)
    ys = r*np.sin(alpha)

    result = list()
    for i in range(node_count):
        loc = Location(x=xs[i], y=ys[i])
        node = Node(id=i, location=loc)

        result.append(node)

    return result
