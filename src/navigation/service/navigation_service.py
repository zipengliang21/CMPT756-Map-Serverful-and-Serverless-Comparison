from flask import Flask
from flask import request

from src.navigation.service.context import CONTEXT
from src.navigation.finder.path import FindPath

app = Flask(__name__)


@app.route("/queryPath", methods=["POST"])
def QueryPath():
    """_summary_

    Returns:
        _type_: _description_
    """
    start_node_id = request.json["start_node_id"]
    dst_node_id = request.json["dst_node_id"]
    result = FindPath(start_node_id, dst_node_id, CONTEXT.db_conn)

    return CONTEXT.encoder.encode(result)
