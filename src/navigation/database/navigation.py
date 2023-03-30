import json
from typing import Set

from src.navigation.database.constant import NAVIGATION_TABLE_NAME
from src.navigation.database.constant import NAVIGATION_TABLE_NODE_ID
from src.navigation.database.constant import NAVIGATION_TABLE_NEIGHBORS
from src.navigation.database.entity import AdjacentEdges
from src.navigation.database.entity import EdgeAttributes


def AddEdges(edges: AdjacentEdges, db_conn) -> None:
    """_summary_

    Args:
        edges (Navigation): _description_
        db_conn (psycopg2.connection): _description_
    """
    query1 = "SELECT {neighbors_col} FROM {table_name}            \
              WHERE {node_id_col}={node_id}".                     \
              format(neighbors_col=NAVIGATION_TABLE_NEIGHBORS,
                     table_name=NAVIGATION_TABLE_NAME,
                     node_id_col=NAVIGATION_TABLE_NODE_ID,
                     node_id=edges.node_id)

    cursor = db_conn.cursor()
    cursor.execute(query1)
    result = cursor.fetchall()
    
    neighbors = dict()
    if len(result) != 0:
        neighbors = result[0][0]

    for dst_node_id, attri in edges.neighbors.items(): 
        neighbors[dst_node_id] =json.dumps( {"dist": attri.distance})

    query2 = "INSERT INTO {table_name} ({node_id_col},              \
                                       {neighbors_col})             \
              VALUES ({node_id}, '{neighbors}')                       \
              ON CONFLICT ({node_id_col})                           \
              DO UPDATE SET                                         \
              {neighbors_col}=excluded.{neighbors_col}".                \
            format(table_name=NAVIGATION_TABLE_NAME,
                   node_id_col=NAVIGATION_TABLE_NODE_ID,
                   neighbors_col=NAVIGATION_TABLE_NEIGHBORS,
                   node_id=edges.node_id,
                   neighbors=json.dumps(neighbors))

    cursor.execute(query2)
    db_conn.commit()


def DeleteEdges(node_id: int, edges: Set[int], db_conn) -> None:
    """_summary_

    Args:
        edges (Navigation): _description_
        db_conn (psycopg2.connection): _description_
    """
    query1 = "SELECT {neighbors_col} FROM {table_name}            \
              WHERE {node_id_col}={node_id}".                     \
              format(neighbors_col=NAVIGATION_TABLE_NEIGHBORS,
                     table_name=NAVIGATION_TABLE_NAME,
                     node_id_col=NAVIGATION_TABLE_NODE_ID,
                     node_id=node_id)

    cursor = db_conn.cursor()
    cursor.execute(query1)
    result = cursor.fetchall()
    if len(result) == 0:
        return

    neighbors = result[0][0]

    for edge in edges:
        if str(edge) in neighbors:
            del neighbors[str(edge)]
    
    query2 = "INSERT INTO {table_name} ({node_id_col},              \
                                       {neighbors_col})             \
              VALUES ({node_id}, '{neighbors}')                       \
              ON CONFLICT ({node_id_col})                           \
              DO UPDATE SET                                         \
              {neighbors_col}=excluded.{neighbors_col}".                \
            format(table_name=NAVIGATION_TABLE_NAME,
                   node_id_col=NAVIGATION_TABLE_NODE_ID,
                   neighbors_col=NAVIGATION_TABLE_NEIGHBORS,
                   node_id=node_id,
                   neighbors=json.dumps(neighbors))

    cursor.execute(query2)
    db_conn.commit()

def findEdges(node_id: int, db_conn) -> Set[int]:
    """_summary_

    Args:
        edges (Navigation): _description_
        db_conn (psycopg2.connection): _description_
    """
    query = "SELECT {neighbors_col} FROM {table_name}            \
             WHERE {node_id_col}={node_id}".                     \
              format(neighbors_col=NAVIGATION_TABLE_NEIGHBORS,
                     table_name=NAVIGATION_TABLE_NAME,
                     node_id_col=NAVIGATION_TABLE_NODE_ID,
                     node_id=node_id)

    cursor = db_conn.cursor()
    cursor.execute(query)
    neighbors = cursor.fetchall()[0][0]

    result = {int(key) for key, _ in neighbors.items()}

    return result