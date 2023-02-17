import requests


def send_request_to_with(node_name, data):
    url = f"http://127.0.0.1:5000/{node_name}"
    response = requests.post(url, json=data)
    return response


# resp = send_request_to_with(
#     "encrypt_file",
#     {
#         "user_id": "1",
#         "file_name": "test.txt",
#         "policy": '("A" and "B")',
#         "content": "This is the data",
#         "attributes": ["A", "B"],
#     },
# )


# resp = send_request_to_with(
#     "decrypt_file",
#     {
#         "user_id": "1",
#         "file_name": "test.txt",
#         "policy": '("A" and "B")',
#         "content": "This is the data",
#         "attributes": ["A", "B"],
#     },
# )

resp = send_request_to_with(
    "delete_file",
    {
        "user_id": "1",
        "file_name": "test.txt",
        "policy": '("A" and "B")',
        "content": "This is the data",
        "attributes": ["A", "B"],
    },
)


print(resp.status_code)
print(resp.json())
