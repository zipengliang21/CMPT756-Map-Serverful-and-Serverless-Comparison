from typing import Dict

class EdgeAttributes:
    def __init__(self, distance: float) -> None:
        self.distance = distance

class AdjacentEdges:
    def __init__(self,
                 node_id: int,
                 neighbors: Dict[int, EdgeAttributes]) -> None:
        assert node_id is not None
        assert neighbors is not None

        self.node_id = node_id
        self.neighbors = neighbors
