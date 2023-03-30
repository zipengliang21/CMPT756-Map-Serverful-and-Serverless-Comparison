from typing import List

class Geolocation:
    def __init__(self,
                 node_id: int,
                 neighbors: List[object]) -> None:
        assert node_id is not None
        assert neighbors is not None

        self.node_id = node_id
        self.neighbors = neighbors
