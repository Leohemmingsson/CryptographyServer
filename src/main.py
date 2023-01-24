# from pip
import flask
from flask import g
import json

# own imports
from mock_abe import rabe

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cryptoType = "abe"


def error_checker(func):
    """
    This function is made for when provided json does not contain all the required keys.
    It is okay to provide more keys than required.
    """

    def wrapper(*args, **kwargs):
        if "abe" not in g:
            g.abe = rabe(cryptoType)

        try:
            res = func(*args, **kwargs)
        except KeyError:
            res = json.dumps(
                {
                    "code": 404,
                    "name": "Key not found",
                    "description": "The provided keys does not match expected keys.",
                }
            )

        return res

    return wrapper


@app.route("/make_file", endpoint="make_file", methods=["POST"])
@error_checker
def make_file():
    """
    POST a JSON containing path and return 200 if ok.
    """
    pass


@app.route("/delete_file", endpoint="delete_file", methods=["POST"])
@error_checker
def delete_file():
    """
    POST a JSON containing path and return 200 if ok.
    """
    pass


@app.route("/encrypt_file", endpoint="encrypt_file", methods=["POST"])
@error_checker
def encrypt_file():
    """
    POST a JSON containing a policy, a file path and a string of text to encrypt, returns 200 if ok.
    """
    data = flask.request.json
    print(data["does not exist"])

    encrypted_data = g.abe.encrypt(data["data"], data["attributes"], g.abe.secret())
    print(encrypted_data)

    return flask.Response({"success": "True"}, status=200, mimetype="text/plain")


@app.route("/decrypt_file", endpoint="decrypt_file", methods=["POST"])
@error_checker
def decrypt_file():
    """
    POST a JSON containing either a user_id or a list of attributes and a file name, returns 200 if ok.
    """
    pass


app.run()
