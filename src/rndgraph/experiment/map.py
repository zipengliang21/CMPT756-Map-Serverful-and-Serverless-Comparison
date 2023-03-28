import math
import random
import matplotlib.pyplot as plt
import sys

class Node:
    def __init__(self, node_id, x, y):
        self.node_id = node_id
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Node {self.node_id}"


class Edge:
    def __init__(self, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = math.sqrt((start_node.x - end_node.x) ** 2 + (start_node.y - end_node.y) ** 2)

    def __lt__(self, other):
        return self.weight < other.weight


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_node_by_id(self, node_id):
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None   

    def get_minimal_spanning_tree(self):
        self.edges.sort()
        parent = dict()
        rank = dict()

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                else:
                    parent[root1] = root2
                    if rank[root1] == rank[root2]:
                        rank[root2] += 1

        for node in self.nodes:
            parent[node] = node
            rank[node] = 0

        minimal_spanning_tree = Graph()
        for edge in self.edges:
            if find(edge.start_node) != find(edge.end_node):
                union(edge.start_node, edge.end_node)
                minimal_spanning_tree.add_node(edge.start_node)
                minimal_spanning_tree.add_node(edge.end_node)
                minimal_spanning_tree.add_edge(edge)

        return minimal_spanning_tree

    def find_shortest_path(self, start_node, end_node):
        visited = set()
        distances = {start_node: 0}
        predecessors = {start_node: None}
        to_visit = [start_node]

        while to_visit:
            current_node = min(to_visit, key=lambda node: distances[node])
            to_visit.remove(current_node)

            if current_node == end_node:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = predecessors[current_node]
                path.reverse()
                return path

            visited.add(current_node)
            for edge in self.edges:
                if edge.start_node == current_node and edge.end_node not in visited:
                    new_distance = distances[current_node] + edge.weight
                    if edge.end_node not in distances or new_distance < distances[edge.end_node]:
                        distances[edge.end_node] = new_distance
                        predecessors[edge.end_node] = current_node
                        to_visit.append(edge.end_node)
                elif edge.end_node == current_node and edge.start_node not in visited:
                    new_distance = distances[current_node] + edge.weight
                    if edge.start_node not in distances or new_distance < distances[edge.start_node]:
                        distances[edge.start_node] = new_distance
                        predecessors[edge.start_node] = current_node
                        to_visit.append(edge.start_node)


    def visualize(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_aspect("equal")
        for node in self.nodes:
            ax.plot(node.x, node.y, "bo")
            ax.annotate(node.node_id, (node.x, node.y))
        for edge in self.edges:
            start_node = edge.start_node
            end_node = edge.end_node
            ax.plot([start_node.x, end_node.x], [start_node.y, end_node.y], "r-")
        plt.show()

    def navigationQuery(self, start_node_id, end_node_id):
        minimal_spanning_tree = self.get_minimal_spanning_tree()
        shortest_path = minimal_spanning_tree.find_shortest_path(self.get_node_by_id(start_node_id), self.get_node_by_id(end_node_id))
        if shortest_path:
            return [node.node_id for node in shortest_path]
        else:
            return None
        
    def updateNode(self, node_id):
        node = self.get_node_by_id(node_id)
        if node is not None:
            r = 100 * math.sqrt(random.uniform(0, 1))
            x = r * math.cos(random.uniform(0, 2 * math.pi))
            y = r * math.sin(random.uniform(0, 2 * math.pi))


if __name__ == "__main__":
    num_nodes = 100
    graph = Graph()
    for node_id in range(num_nodes):
        r = 100 * math.sqrt(random.uniform(0, 1))
        x = r * math.cos(random.uniform(0, 2 * math.pi))
        y = r * math.sin(random.uniform(0, 2 * math.pi))

        node = Node(node_id, x, y)
        graph.add_node(node)

    for i, start_node in enumerate(graph.nodes):
        for end_node in graph.nodes[i + 1:]:
            edge = Edge(start_node, end_node)
            graph.add_edge(edge)

    minimal_spanning_tree = graph.get_minimal_spanning_tree()

    if len(sys.argv) == 1:
        start_node = minimal_spanning_tree.nodes[0]
        end_node = minimal_spanning_tree.nodes[-1]
    elif len(sys.argv) == 2:
        raise ValueError("Error: Please provide two node IDs.")
    elif len(sys.argv) == 3:
        start_node_id = int(sys.argv[1])
        end_node_id = int(sys.argv[2])
        start_node = graph.get_node_by_id(start_node_id)
        end_node = graph.get_node_by_id(end_node_id)

    shortest_path = minimal_spanning_tree.find_shortest_path(start_node, end_node)
    print(f"Shortest path: {[node.node_id for node in shortest_path]}")

    # Visualize the minimal spanning tree and shortest path
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")
    ax.set_title("Minimal Spanning Tree and Shortest Path")

    for node in graph.nodes:
        ax.plot(node.x, node.y, "bo")
        ax.annotate(str(node.node_id), (node.x, node.y))

    for edge in minimal_spanning_tree.edges:
        start_node = edge.start_node
        end_node = edge.end_node
        ax.plot([start_node.x, end_node.x], [start_node.y, end_node.y], "r-")

    for i in range(len(shortest_path) - 1):
        start_node = shortest_path[i]
        end_node = shortest_path[i + 1]
        ax.plot([start_node.x, end_node.x], [start_node.y, end_node.y], "g-", linewidth=2)

    path_str = " -> ".join([str(node.node_id) for node in shortest_path])
    ax.text(0, -130, f"Shortest path: {path_str}", fontsize=12, horizontalalignment="center")

    plt.show()



