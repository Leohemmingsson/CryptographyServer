import requests


def send_request_to_with(node_name, data):
    # url = f"http://31.208.238.201:59931/{node_name}"
    url = f"http://127.0.0.1:5000/{node_name}"
    response = requests.post(url, json=data)
    return response


def get_post_data():
    return {
        "user_id": "5",
        "file_name": "test.txt",
        "policy": '"A" and "B"',
        "content": "A secret message",
        "attributes": ["A", "B"],
    }


def encrypt_file(data):
    resp = send_request_to_with("encrypt_file", data)
    return resp


def decrypt_file(data):
    resp = send_request_to_with("decrypt_file", data)
    return resp


def delete_file(data):
    resp = send_request_to_with("delete_file", data)
    return resp


def get_static(data):
    resp = send_request_to_with("get_static", data)
    return resp


resp = decrypt_file(get_post_data())
print(resp.status_code)
print(resp.json())
