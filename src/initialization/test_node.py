import unittest

from src.initialization.node import Location
from src.initialization.node import Node
from src.initialization.node import EuclideanDistance
from src.initialization.node import GenerateNodes


class TestNode(unittest.TestCase):

    def test_EuclideanDistance(self):
        a = Node(id=0, location=Location(x=1, y=1))
        b = Node(id=0, location=Location(x=2, y=0))

        self.assertAlmostEqual(
            first=EuclideanDistance(a=a, b=a), second=0)

        self.assertAlmostEqual(
            first=EuclideanDistance(a=a, b=b),
            second=1.414213562,
            places=2)

    def test_GenerateNodes_NodeCount(self):
        nodes = GenerateNodes(node_count=0, radius=10)
        self.assertTrue(len(nodes) == 0)

        nodes = GenerateNodes(node_count=5, radius=10)
        self.assertTrue(len(nodes) == 5)

    def test_GenerateNodes_Idempotence(self):
        nodes = GenerateNodes(node_count=1, radius=10)
        nodes2 = GenerateNodes(node_count=1, radius=10)
        self.assertTrue(nodes[0].location.x == nodes2[0].location.x)
        self.assertTrue(nodes[0].location.y == nodes2[0].location.y)

    def test_GenerateNodes_Ids(self):
        nodes = GenerateNodes(node_count=3, radius=10)

        ids = set()
        for node in nodes:
            ids.add(node.id)

        self.assertTrue(len(ids) == 3)

    def test_GenerateNodes_Radius(self):
        RADIUS = 10

        nodes = GenerateNodes(node_count=1000, radius=RADIUS)
        origin = Node(id=-1, location=Location(x=0, y=0))

        for node in nodes:
            self.assertTrue(EuclideanDistance(a=origin, b=node) < RADIUS)


if __name__ == '__main__':
    unittest.main()
