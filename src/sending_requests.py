import requests

url = "http://127.0.0.1:5000" + "/encrypt_file"
# url = "http://127.0.0.1:5000" + "/decrypt_file"
# url = "http://127.0.0.1:5000" + "/test"

# post json to url
data = {
    "content": "This is the data",
    "policy": {"area": "testing", "access": 2},
    "name": "test.txt",
    "id": 1,
}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
