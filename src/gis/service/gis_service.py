from flask import Flask

from src.gis.service.context import CONTEXT

app = Flask(__name__)


@app.route("/topology", methods=["GET"])
def GetTopology():
    """_summary_

    Returns:
        _type_: _description_
    """
    result = CONTEXT.map_reader.Query()
    return CONTEXT.encoder.encode(result)
