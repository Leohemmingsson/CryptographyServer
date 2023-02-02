import requests

def send_request_to_with(node_name, data):
    url = f"http://127.0.0.1:5000/{node_name}"
    response = requests.post(url, json=data)
    return response


def test_node(node_name: str):
    data = {
        "content": "This is the data",
        "policy": {"area": "testing", "access": 2},
        "file_name": "test.txt",
        "user_id": 1,
    }
    response = send_request_to_with(node_name, data)

    print(response.status_code)
    print(response.json())


def test_all_nodes(nodes: list):
    for node in nodes:
        test_node(node)
    


test_all_nodes(["make_file", "encrypt_file", "decrypt_file", "delete_file"])

