from json import JSONEncoder

from src.navigation.database.connection import CreateDatabaseConnection


class DictJSONEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class NavigationServiceContext:
    """_summary_
    """

    def __init__(self) -> None:
        self.db_conn = None
        self.encoder = DictJSONEncoder()

    def Init(self,
             navigation_db_host: str,
             navigation_db_user: str,
             navigation_db_password: str) -> None:
        """_summary_

        Args:
            gis_db_host (str): _description_
            gis_db_user (str): _description_
            gis_db_password (str): _description_
        """
        self.db_conn = CreateDatabaseConnection(
            navigation_db_host=navigation_db_host,
            navigation_db_user=navigation_db_user,
            navigation_db_password=navigation_db_password)


CONTEXT = NavigationServiceContext()
