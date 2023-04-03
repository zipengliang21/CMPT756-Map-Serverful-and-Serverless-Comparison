import unittest

from src.gis.mutation.writer import CollectGeolocations
from src.gis.mutation.writer import CollectTopology
from src.mutation.proto_py.mutation_pb2 import MutationRequest
from src.mutation.proto_py.mutation_pb2 import DeleteUndirectedEdgeRequest
from src.mutation.proto_py.mutation_pb2 import WriteUndirectedEdgeRequest
from src.mutation.proto_py.mutation_pb2 import Node


class TestWriter(unittest.TestCase):
    def test_CollectGeolocations(self):
        node_1 = Node(id=1,
                      location=Node.Location(x=10, y=100),
                      importance=0.1)
        node_2 = Node(id=2,
                      location=Node.Location(x=20, y=200),
                      importance=0.2)
        node_3 = Node(id=3,
                      location=Node.Location(x=30, y=300),
                      importance=0.3)

        write_edge1 = WriteUndirectedEdgeRequest(node_a=node_1, node_b=node_2)
        write_edge2 = WriteUndirectedEdgeRequest(node_a=node_1, node_b=node_3)
        write_edge3 = WriteUndirectedEdgeRequest(node_a=node_2, node_b=node_3)
        write_edge4 = WriteUndirectedEdgeRequest(node_a=node_3, node_b=node_3)

        requests = [
            MutationRequest(write_edge=write_edge1),
            MutationRequest(write_edge=write_edge2),
            MutationRequest(write_edge=write_edge3),
            MutationRequest(write_edge=write_edge4),
        ]

        locs = CollectGeolocations(requests=requests)
        self.assertEqual(3, len(locs))

        self.assertTrue(1 in locs)
        self.assertTrue(2 in locs)
        self.assertTrue(3 in locs)

        self.assertTrue(locs[1].id == 1)
        self.assertTrue(locs[2].id == 2)
        self.assertTrue(locs[3].id == 3)

        self.assertTrue(locs[1].x == 10)
        self.assertTrue(locs[2].x == 20)
        self.assertTrue(locs[3].x == 30)

        self.assertTrue(locs[1].y == 100)
        self.assertTrue(locs[2].y == 200)
        self.assertTrue(locs[3].y == 300)

        self.assertAlmostEqual(0.1, locs[1].importance, places=2)
        self.assertAlmostEqual(0.2, locs[2].importance, places=2)
        self.assertAlmostEqual(0.3, locs[3].importance, places=2)

    def test_CollectTopology(self):
        node_1 = Node(id=1,
                      location=Node.Location(x=10, y=100),
                      importance=0.1)
        node_2 = Node(id=2,
                      location=Node.Location(x=20, y=200),
                      importance=0.2)
        node_3 = Node(id=3,
                      location=Node.Location(x=30, y=300),
                      importance=0.3)

        write_edge1 = WriteUndirectedEdgeRequest(node_a=node_1, node_b=node_2)
        write_edge2 = WriteUndirectedEdgeRequest(node_a=node_1, node_b=node_3)
        write_edge3 = WriteUndirectedEdgeRequest(node_a=node_2, node_b=node_3)
        write_edge4 = WriteUndirectedEdgeRequest(node_a=node_3, node_b=node_2)

        delete_edge1 = DeleteUndirectedEdgeRequest(node_a_id=2, node_b_id=1)
        delete_edge2 = DeleteUndirectedEdgeRequest(node_a_id=1, node_b_id=4)

        requests = [
            MutationRequest(write_edge=write_edge1),
            MutationRequest(write_edge=write_edge2),
            MutationRequest(write_edge=write_edge3),
            MutationRequest(write_edge=write_edge4),

            MutationRequest(delete_edge=delete_edge1),
            MutationRequest(delete_edge=delete_edge2),
        ]

        collection = CollectTopology(requests=requests)

        self.assertEqual(4, len(collection.additions))
        self.assertEqual(2, len(collection.deletions))

        self.assertTrue((1, 3) in collection.additions)
        self.assertTrue((3, 1) in collection.additions)
        self.assertTrue((2, 3) in collection.additions)
        self.assertTrue((3, 2) in collection.additions)

        self.assertTrue((1, 4) in collection.deletions)
        self.assertTrue((4, 1) in collection.deletions)


if __name__ == '__main__':
    unittest.main()
