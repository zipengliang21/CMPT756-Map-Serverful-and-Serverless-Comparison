from typing import List

from src.gis.database.constant import GEOLOCATION_TABLE_NAME
from src.gis.database.constant import GEOLOCATION_TABLE_ID
from src.gis.database.constant import GEOLOCATION_TABLE_X
from src.gis.database.constant import GEOLOCATION_TABLE_Y
from src.gis.database.constant import GEOLOCATION_TABLE_IMPORTANCE
from src.gis.database.constant import TOPOLOGY_TABLE_NAME
from src.gis.database.constant import TOPOLOGY_TABLE_LOC1_ID
from src.gis.database.constant import TOPOLOGY_TABLE_LOC2_ID
from src.gis.database.constant import TOPOLOGY_TABLE_DISTANCE
from src.gis.database.entity import Geolocation
from src.gis.database.entity import Topology


def ReadGeolocations(db_conn) -> List[Geolocation]:
    """_summary_

    Args:
        db_conn (_type_): _description_

    Returns:
        List[Geolocation]: _description_
    """
    query = f"SELECT                            \
                {GEOLOCATION_TABLE_ID},         \
                {GEOLOCATION_TABLE_X},          \
                {GEOLOCATION_TABLE_Y},          \
                {GEOLOCATION_TABLE_IMPORTANCE}  \
            FROM {GEOLOCATION_TABLE_NAME} "

    cursor = db_conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    result = list()
    for row in rows:
        geolocation = Geolocation(id=row[0],
                                  x=row[1],
                                  y=row[2],
                                  importance=row[3])
        result.append(geolocation)

    return result


def ReadTopology(db_conn) -> List[Topology]:
    """_summary_

    Args:
        db_conn (_type_): _description_

    Returns:
        List[Topology]: _description_
    """
    query = f"SELECT                        \
                {TOPOLOGY_TABLE_LOC1_ID},   \
                {TOPOLOGY_TABLE_LOC2_ID},   \
                {TOPOLOGY_TABLE_DISTANCE}   \
            FROM {TOPOLOGY_TABLE_NAME} "

    cursor = db_conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    result = list()
    for row in rows:
        geolocation = Topology(loc1_id=row[0],
                               loc2_id=row[1],
                               distance=row[2])
        result.append(geolocation)

    return result
