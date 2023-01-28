# from pip
import flask
from flask import g
import json

# from pip git
import require

# own imports
from mock_abe import rabe
from database_abstraction import DB

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cryptoType = "abe"


def return_value(func):
    """
    Appropriate response
    """

    def wrapper(*args, **kwargs):
        if "sql" not in g:
            g.sql = DB("AC17")

        return_value = func(*args, **kwargs)

        if type(return_value) is str:
            return flask.make_response(return_value, json.loads(return_value)["status"])

        if len(return_value) > 2:
            response = flask.jsonify(Name=return_value[0], Description=return_value[2])
        else:
            response = flask.jsonify(Name=return_value[0])

        return flask.make_response(response, return_value[1])

    return wrapper


@app.route("/make_file", endpoint="make_file", methods=["POST"])
def make_file():
    """
    POST a JSON containing path and return 200 if ok.
    """
    data = flask.request.json
    exec_res = g.sql.create_file(id=data["id"])
    res = ("", 200) if exec_res == True else ("", 400)
    return res


@app.route("/delete_file", endpoint="delete_file", methods=["POST"])
def delete_file():
    """
    POST a JSON containing path and return 200 if ok.
    """
    data = flask.request.json
    exec_res = g.sql.delete_file(id=data["id"])
    res = ("", 200) if exec_res == True else ("", 400)
    return res


@app.route("/encrypt_file", endpoint="encrypt_file", methods=["POST"])
@return_value
@require.fields(flask.request)
def encrypt_file(content: str, policy: str, path: str):
    """
    POST a JSON containing a policy, a file path and a string of text to encrypt, returns 200 if ok.
    """

    encrypted_data = g.abe.encrypt(
        content=content, policy=policy, secret_key=g.abe.secret()
    )

    exec_res = g.sql.post(path=path, file=encrypted_data)

    res = ("", 200) if exec_res == True else ("", 400)

    return res


@app.route("/decrypt_file", endpoint="decrypt_file", methods=["POST"])
def decrypt_file():
    """
    POST a JSON containing either a user_id or a list of attributes and a file name, returns 200 if ok.
    """
    data = flask.request.json
    pass


app.run()
