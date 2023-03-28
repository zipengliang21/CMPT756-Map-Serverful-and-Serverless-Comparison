import psycopg2.extras as pge
from typing import Dict
from typing import Set
from typing import Tuple

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


def WriteGeolocations(locations: Dict[int, Geolocation], db_conn) -> None:
    """_summary_

    Args:
        locations (List[Geolocation]): _description_
        db_conn (psycopg2.connection): _description_
    """
    query = "INSERT INTO {table_name} ({id},                    \
                                       {x},                     \
                                       {y},                     \
                                       {importance}) VALUES %s  \
                 ON CONFLICT ({id})                             \
                 DO UPDATE SET                                  \
                    {x}=excluded.{x},                           \
                    {y}=excluded.{y},                           \
                    {importance}=excluded.{importance}".        \
            format(table_name=GEOLOCATION_TABLE_NAME,
                   id=GEOLOCATION_TABLE_ID,
                   x=GEOLOCATION_TABLE_X,
                   y=GEOLOCATION_TABLE_Y,
                   importance=GEOLOCATION_TABLE_IMPORTANCE)

    cursor = db_conn.cursor()

    rows_to_insert = list()
    for _, location in locations.items():
        rows_to_insert.append((
            location.id,
            location.x,
            location.y,
            location.importance,
        ))

    pge.execute_values(cur=cursor,
                       sql=query,
                       argslist=rows_to_insert,
                       template=None)
    db_conn.commit()


def WriteTopology(topology: Dict[Tuple[int, int], Topology], db_conn) -> None:
    """_summary_

    Args:
        topology (Dict[Tuple[int, int], Topology]): _description_
        db_conn (_type_): _description_
    """
    query = "INSERT INTO {table_name} ({loc1_id},               \
                                       {loc2_id},               \
                                       {distance}) VALUES %s    \
                 ON CONFLICT ({loc1_id}, {loc2_id})             \
                 DO UPDATE SET                                  \
                    {loc1_id}=excluded.{loc1_id},               \
                    {loc2_id}=excluded.{loc2_id},               \
                    {distance}=excluded.{distance}".            \
            format(table_name=TOPOLOGY_TABLE_NAME,
                   loc1_id=TOPOLOGY_TABLE_LOC1_ID,
                   loc2_id=TOPOLOGY_TABLE_LOC2_ID,
                   distance=TOPOLOGY_TABLE_DISTANCE)

    cursor = db_conn.cursor()

    rows_to_insert = list()
    for _, t in topology.items():
        rows_to_insert.append((
            t.loc1_id,
            t.loc2_id,
            t.distance,
        ))

    pge.execute_values(cur=cursor,
                       sql=query,
                       argslist=rows_to_insert,
                       template=None)
    db_conn.commit()


def DeleteTopology(links: Set[Tuple[int, int]], db_conn) -> None:
    """_summary_

    Args:
        links (Set[Tuple[int, int]]): _description_
        db_conn (_type_): _description_
    """
    cursor = db_conn.cursor()

    for link in links:
        query = "DELETE FROM {table_name}           \
                WHERE {loc1_id_col}={loc1_id} AND   \
                      {loc2_id_col}={loc2_id} ".      \
                format(table_name=TOPOLOGY_TABLE_NAME,
                       loc1_id_col=TOPOLOGY_TABLE_LOC1_ID,
                       loc2_id_col=TOPOLOGY_TABLE_LOC2_ID,
                       loc1_id=link[0],
                       loc2_id=link[1])

        cursor.execute(query)

    db_conn.commit()
