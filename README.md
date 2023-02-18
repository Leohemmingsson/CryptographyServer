# CryptographyServer
This is a flask server that is supposed to be a api for ABE (Attribute Based Encryption) schemes. 
The server is written in python flask and is connected to through a sql server for content management.


# How to start the server:
1. Create a .env file for DB connection:
```
SERVER_IP=<IP>
DB_USER=<UserName>
DB_PASS=<Password>
DATABASE=<DatabaseName>
```
2. install dependencies from requirements.txt (`pip install -r requirements.txt`)
3. Run main.py (`python src/main.py`)

# Sending requests to the server
```python
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
```
