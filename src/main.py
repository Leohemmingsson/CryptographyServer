# from pip
import flask
import json

# own imports
from mock_abe import rabe

# flask server with json post for path/make_file
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/make_file", methods=["POST"])
def make_file():
    data = flask.request.json

    handle = rabe(data["type"])
    encrypted_data = handle.encrypt(data["data"], data["attributes"], handle.secret())

    return flask.Response({"success": "True"}, status=200, mimetype="text/plain")


# rest route  for path/hi
@app.route("/hi", methods=["GET"])
def hi():
    return "hi"


app.run()
