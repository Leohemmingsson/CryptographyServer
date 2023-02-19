import requests


def send_request_to_with(node_name, data):
    url = f"http://127.0.0.1:5000/{node_name}"
    response = requests.post(url, json=data)
    return response


def get_post_data():
    {
        "user_id": "1",
        "file_name": "test.txt",
        "policy": '("A" and "B")',
        "content": "This is the data",
        "attributes": ["A", "B"],
    },


def encrypt_file(data):
    resp = send_request_to_with("encrypt_file", data)
    return resp


def decrypt_file(data):
    resp = send_request_to_with("decrypt_file", data)
    return resp


def delete_file(data):
    resp = send_request_to_with("delete_file", data)
    return resp


resp = encrypt_file(get_post_data())
print(resp.status_code)
print(resp.json())
