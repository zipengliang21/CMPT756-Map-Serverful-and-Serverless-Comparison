
class Geolocation:
    def __init__(self,
                 id: int,
                 x: float,
                 y: float,
                 importance: float) -> None:
        assert id is not None
        assert x is not None
        assert y is not None
        assert importance is not None

        self.id = id
        self.x = x
        self.y = y
        self.importance = importance


class Topology:
    def __init__(self,
                 loc1_id: int,
                 loc2_id: int,
                 distance: float) -> None:
        assert loc1_id is not None
        assert loc2_id is not None

        self.loc1_id = loc1_id
        self.loc2_id = loc2_id
        self.distance = distance
