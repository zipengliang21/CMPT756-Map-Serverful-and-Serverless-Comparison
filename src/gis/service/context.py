from json import JSONEncoder

from src.gis.database.connection import CreateDatabaseConnection
from src.gis.query.reader import MapReader


class DictJSONEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class GisServiceContext:
    """_summary_
    """

    def __init__(self) -> None:
        self.map_reader: MapReader = None
        self.encoder = DictJSONEncoder()

    def Init(self,
             gis_db_host: str,
             gis_db_password: str) -> None:
        """_summary_

        Args:
            gis_db_host (str): _description_
            gis_db_password (str): _description_
        """
        db_conn = CreateDatabaseConnection(
            gis_db_host=gis_db_host,
            gis_db_password=gis_db_password)

        self.map_reader = MapReader(db_conn=db_conn)


CONTEXT = GisServiceContext()
