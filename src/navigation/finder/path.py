from typing import List
from collections import deque

from src.navigation.database.navigation import findEdges

def FindPath(start_node_id: int, dst_node_id: int, db_conn) -> List[int]:
    visited = set()
    parent = {}
    queue = deque([start_node_id])
    visited.add(start_node_id)
    parent[start_node_id] = None

    while queue:
        curr_node_id = queue.popleft()

        if curr_node_id == dst_node_id:
            # Reconstruct path from parent pointers
            path = []
            node = dst_node_id
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor in findEdges(curr_node_id, db_conn):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = curr_node_id
                queue.append(neighbor)

    # If the destination node is not reachable from the start node, return an empty list
    return []

if __name__ == '__main__':
    print(FindPath())
