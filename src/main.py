# from pip
from flask import g, Flask, make_response, request
import json

# from pip git
import require

# local imports
from cryptography import ABE, CPAc17
from database_abstraction import DB
from rabe_py import ac17 as rac17

app = Flask(__name__)
app.config["DEBUG"] = True


def __http_response(name="", description="", code=200, content=None, content_type=None):
    formatter_response = {"name": name, "description": description}
    if content and content_type:
        formatter_response["content"] = content
        formatter_response["content_type"] = content_type

    return make_response(json.dumps(formatter_response), code)

# This is bad practice, but we need the static keys

ac17 = ABE(CPAc17)
ac17.generate_static_keys()

# When server starts


@app.before_request
def init():
    cryptoType = "AC17-cp"
    g.sql = DB()


@app.teardown_appcontext
def teardown(exception):
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
    global ac17
    ac17.policy = policy
    ac17.generate_static_keys()
    encrypted_data = str(ac17.encrypt(
        plaintext=content
    ))
    exec_res = g.sql.post(
        user_id=user_id, file_name=file_name, content=encrypted_data)

    res = {"code": 200} if exec_res else {"code": 400}

    return res


@app.route("/decrypt_file", endpoint="decrypt_file", methods=["POST"])
@require.fields(request)
def decrypt_file(user_id: int, attributes: list[str], file_name: str):
    """
    POST a JSON containing either a user_id or a list of attributes and a file name, returns 200 if ok.
    """
    global ac17
    ac17.attributes = attributes
    ac17.keygen()
    file = g.sql.get(user_id=user_id, file_name=file_name,
                     attributes=attributes)
    file = rac17.PyAc17CpCiphertext(file)
    decrypt_file = str(ac17.decrypt(
        ciphertext=file
    ))
    return decrypt_file, 200


app.run(host="0.0.0.0")
