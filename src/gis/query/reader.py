
from typing import List

from src.gis.database.entity import Geolocation
from src.gis.database.entity import Topology
from src.gis.database.query import ReadGeolocations
from src.gis.database.query import ReadTopology


class MapQueryResult:
    """_summary_
    """

    def __init__(self,
                 geolocations: List[Geolocation],
                 topology: List[Topology]) -> None:
        """_summary_

        Args:
            geolocations (List[Geolocation]): _description_
            topology (List[Topology]): _description_
        """
        self.geolocations = geolocations
        self.topology = topology


class MapReader:
    def __init__(self, db_conn) -> None:
        """_summary_

        Args:
            db_conn (_type_): _description_
        """
        self.db_conn = db_conn

    def Query(self) -> MapQueryResult:
        """_summary_

        Returns:
            MapQueryResult: _description_
        """
        geolocations = ReadGeolocations(db_conn=self.db_conn)
        topology = ReadTopology(db_conn=self.db_conn)

        return MapQueryResult(
            geolocations=geolocations,
            topology=topology)
