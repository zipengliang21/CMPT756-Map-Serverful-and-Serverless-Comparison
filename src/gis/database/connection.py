from psycopg2 import connect

from src.gis.database.constant import GIS_DATABASE_NAME
from src.gis.database.constant import GIS_DATABASE_USER


def CreateDatabaseConnection(gis_db_host: str, gis_db_password: str):
    """_summary_

    Args:
        gis_db_host (str): _description_
        gis_db_password (str): _description_

    Returns:
        _type_: _description_
    """
    conn_params = "host='{host}' dbname='{dbname}'          \
                   user='{user}' password='{password}'".  \
        format(
            host=gis_db_host,
            dbname=GIS_DATABASE_NAME,
            user=GIS_DATABASE_USER,
            password=gis_db_password
        )

    return connect(conn_params)
