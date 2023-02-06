# from pip
import flask
from flask import g, Flask, make_response, request
import json

# from pip git
import require

# local imports
from mock_abe import rabe
from database_abstraction import DB

app = Flask(__name__)
app.config["DEBUG"] = True


def __http_response(name="", description="", code=200, content=None, content_type=None):
    formatter_response = {"name": name, "description": description}
    if content and content_type:
        formatter_response["content"] = content
        formatter_response["content_type"] = content_type

    return make_response(json.dumps(formatter_response), code)


# When server starts
@app.before_request
def init():
    print("hello")
    cryptoType = "AC17-cp"
    g.abe = rabe(cryptoType)
    g.sql = DB()


@app.teardown_appcontext
def teardown(exception):
    print("teardown")
    g.pop("abe")
    g.sql.close()
    g.pop("sql")


@app.route("/make_file", endpoint="make_file", methods=["POST"])
@require.fields(request, response_formatter=__http_response)
def make_file(user_id: str, file_name: str):
    """
    POST a JSON containing path and return 200 if ok.
    """
    exec_res = g.sql.create_file(user_id, file_name)
    res = {"code": 200} if exec_res == True else {"code": 400}
    return res


@app.route("/delete_file", endpoint="delete_file", methods=["POST"])
@require.fields(request, response_formatter=__http_response)
def delete_file(user_id: str, file_name: str):
    """
    POST a JSON containing path and return 200 if ok.
    """
    exec_res = g.sql.delete_file(user_id, file_name)
    res = {"code": 200} if exec_res == True else {"code": 400}
    return res


@app.route("/encrypt_file", endpoint="encrypt_file", methods=["POST"])
@require.fields(request, response_formatter=__http_response)
def encrypt_file(user_id: int, policy: str, file_name: str, content: str):
    """
    POST a JSON containing a policy, a file path and a string of text to encrypt, returns 200 if ok.
    """
    public_key = g.sql.get_public_key()
    encrypted_data = g.abe.encrypt(public_key=public_key ,content=content, policy=policy)

    exec_res = g.sql.post(user_id=user_id, file_name=file_name, content=content)
    print("This should have worked")
    res = {"code": 200} if exec_res else {"code": 400}

    return res


@app.route("/decrypt_file", endpoint="decrypt_file", methods=["POST"])
@require.fields(request)
def decrypt_file(user_id: int, attributes: str, file_name: str):
    """
    POST a JSON containing either a user_id or a list of attributes and a file name, returns 200 if ok.
    """
    print("Decrypt call")
    file = g.sql.get(user_id=user_id,file_name=file_name,attributes=attributes)
    return file,200


app.run(host="0.0.0.0")
