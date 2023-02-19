# from pip
from flask import g, Flask, make_response, request
from json import dumps

# from pip git
import require

# local imports
from abe_abstraction import *
from database_abstraction import DB
from rabe_py import ac17

app = Flask(__name__)
app.config["DEBUG"] = True


def __http_response(name="", description="", code=200, content=None, content_type=None):
    formatter_response = {"name": name, "description": description}
    if content and content_type:
        formatter_response["content"] = content
        formatter_response["content_type"] = content_type

    return make_response(dumps(formatter_response), code)


# When server starts
@app.before_request
def init():
    g.abe = ABE(KPAc17)
    g.sql = DB()


@app.teardown_appcontext
def teardown(exception):
    g.pop("abe")
    g.sql.close()
    g.pop("sql")


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
    if not g.abe.load_static_keys_from_sql(g.sql):
        # Need new keys
        pass
    if policy != None:
        g.abe.set_policy(policy)
    if attributes != None:
        g.abe.set_attributes(attributes)

    encrypted_data = g.abe.encrypt(plaintext=content)

    exec_res = g.sql.post_file(
        user_id=user_id, file_name=file_name, content=str(encrypted_data)
    )

    res = {"code": 200} if exec_res else {"code": 400}

    return res


@app.route("/decrypt_file", endpoint="decrypt_file", methods=["POST"])
@require.fields(request, response_formatter=__http_response)
def decrypt_file(
    user_id: int, file_name: str, attributes: str = None, policy: str = None
):
    """
    POST a JSON containing either a user_id or a list of attributes and a file name, returns 200 if ok.
    """
    if not g.abe.load_static_keys_from_sql(g.sql):
        # If there is no static keys, there should not be any files as well
        return {"code": 400, "description": "No static keys found."}

    if policy != None:
        g.abe.set_policy(policy)
    if attributes != None:
        g.abe.set_attributes(attributes)

    ciphertext = g.sql.get_file(user_id=user_id, file_name=file_name)
    g.abe.keygen()

    plaintext = g.abe.decrypt(ciphertext=ciphertext)

    return {"code": 200, "content": plaintext, "content_type": "text/plain"}


app.run()
