from flask import Flask

from src.gis.service.context import CONTEXT

app = Flask(__name__)


@app.route("/", methods=["GET"])
def HealthCheck():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "{}"


@app.route("/topology", methods=["GET"])
def GetTopology():
    """_summary_

    Returns:
        _type_: _description_
    """
    result = CONTEXT.map_reader.Query()
    return CONTEXT.encoder.encode(result)
