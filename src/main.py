# from pip
import flask
from flask import g
import json

# from pip git
import require

# local imports
from mock_abe import rabe
from database_abstraction import DB

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def __http_response(name="", description="", code=200, content=None, content_type=None):
    formatter_response = {"name": name, "description": description}
    if content and content_type:
        formatter_response["content"] = content
        formatter_response["content_type"] = content_type

    return flask.make_response(json.dumps(formatter_response), code)


# When server starts
@app.before_request
def init():
    print("hello")
    cryptoType = "abe"
    g.abe = rabe(cryptoType)
    g.sql = DB()


@app.teardown_appcontext
def teardown(exception):
    print("teardown")
    g.pop("abe")
    g.sql.close()
    g.pop("sql")


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
    res = {"code": 200} if exec_res == True else {"code": 400}
    return res


@app.route("/encrypt_file", endpoint="encrypt_file", methods=["POST"])
@require.fields(flask.request, response_formatter=__http_response)
def encrypt_file(content: str, policy: str, id: int, name: str):
    """
    POST a JSON containing a policy, a file path and a string of text to encrypt, returns 200 if ok.
    """
    if "abe" in g:
        print("abe exists")
    else:
        print("NO")

    encrypted_data = g.abe.encrypt(
        content=content, policy=policy, secret_key=g.abe.setup()
    )

    exec_res = g.sql.post(id=id, name=name, file=encrypted_data)

    res = {"code": 200} if exec_res else {"code": 400}

    return res


@app.route("/decrypt_file", endpoint="decrypt_file", methods=["POST"])
@require.fields(flask.request, response_formatter=__http_response)
def decrypt_file():
    """
    POST a JSON containing either a user_id or a list of attributes and a file name, returns 200 if ok.
    """
    if "abe" in g:
        print("abe exists")
    else:
        print("NO")

    return {"code": 200}


app.run()
