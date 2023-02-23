# from pip
from flask import g, Flask, make_response, request
from json import dumps

# from pip git
import require

# local imports
from abe_abstraction import *
from database_abstraction import DB

app = Flask(__name__)
app.config["DEBUG"] = True


def __http_response(name="", description="", code=200, content=None, content_type=None):
    formatter_response = {"name": name, "description": description}
    if content and content_type:
        formatter_response["content"] = content
        formatter_response["content_type"] = content_type

    return make_response(dumps(formatter_response), code)


# Before *each* request
@app.before_request
def init():
    g.abe = ABE(CPAc17)
    g.sql = DB()


# This happens after *each* request
@app.teardown_appcontext
def teardown(exception):
    g.pop("abe")
    g.sql.close()
    g.pop("sql")


@app.route("/encrypt_file", endpoint="encrypt_file", methods=["POST"])
@require.fields(request, response_formatter=__http_response)
def encrypt_file(
    user_id: int,
    file_name: str,
    content: str,
    policy: str = None,
    attributes: str = None,
):
    """
    POST a JSON containing a policy, a file path and a string of text to encrypt, returns 200 if ok.
    """
    try:
        __encrypt_file_func(user_id, file_name, content, policy, attributes)
        res = {"code": 200, "description": "File was created"}

    except Exception as e:
        res = {"code": 400, "description": str(e)}

    return res


@app.route("/decrypt_file", endpoint="decrypt_file", methods=["POST"])
@require.fields(request, response_formatter=__http_response)
def decrypt_file(
    user_id: int, file_name: str, attributes: str = None, policy: str = None
):
    """
    POST a JSON containing either a user_id or a list of attributes and a file name, returns 200 if ok.
    """
    try:
        plaintext = __decrypt_file_fun(user_id, file_name, attributes, policy)
        res = {"code": 200, "content": plaintext, "content_type": "text/plain"}
    except Exception as e:
        res = {"code": 400, "description": str(e)}

    return res


@app.route("/delete_file", endpoint="delete_file", methods=["POST"])
@require.fields(request, response_formatter=__http_response)
def delete_file(user_id: str, file_name: str):
    """
    POST a JSON containing path and return 200 if ok.
    """
    try:
        g.sql.delete_file(user_id, file_name)
        res = {"code": 200, "description": "File has been removed"}

    except Exception as e:
        res = {"code": 400, "description": str(e)}
    return res


def __encrypt_file_func(user_id, file_name, content, policy=None, attributes=None):
    """
    Function that encrypts a file and stores it in the database.
    """
    # Getting values from flask global values
    abe_handle = g.abe
    sql_handle = g.sql

    abe_handle.load_static_keys_from_sql(sql_handle)

    if policy != None:
        abe_handle.set_policy(policy)
    if attributes != None:
        abe_handle.set_attributes(attributes)

    encrypted_data = abe_handle.encrypt(content, user_id)
    sql_handle.post_file(user_id, file_name, str(encrypted_data))


def __decrypt_file_fun(user_id, file_name, attributes, policy):
    """
    Function that decrypts a file and returns the plaintext.
    """
    # Getting values from flask global values
    abe_handle = g.abe
    sql_handle = g.sql

    abe_handle.load_static_keys_from_sql(sql_handle)

    if policy != None:
        abe_handle.set_policy(policy)
    if attributes != None:
        abe_handle.set_attributes(attributes)

    ciphertext = abe_handle.get_file(user_id=user_id, file_name=file_name)

    plaintext = abe_handle.decrypt(ciphertext, user_id)

    return plaintext


app.run()
