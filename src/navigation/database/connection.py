from psycopg2 import connect

from src.navigation.database.constant import NAVIGATION_DATABASE_NAME
from src.navigation.database.constant import NAVIGATION_DATABASE_USER


def CreateDatabaseConnection(navigation_db_host: str, navigation_db_password: str):
    """_summary_

    Args:
        navigation_db_host (str): _description_
        navigation_db_password (str): _description_

    Returns:
        _type_: _description_
    """
    conn_params = "host='{host}' dbname='{dbname}'          \
                   user='{user}' password='{password}'".  \
        format(
            host=navigation_db_host,
            dbname=NAVIGATION_DATABASE_NAME,
            user=NAVIGATION_DATABASE_USER,
            password=navigation_db_password
        )

    return connect(conn_params)
