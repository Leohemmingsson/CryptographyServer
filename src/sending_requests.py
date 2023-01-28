import requests

url = "http://127.0.0.1:5000" + "/encrypt_file"

# post json to url
data = {
    "content": "This is the data",
    "policy": {"area": "testing", "access": 2},
    "path": "test.txt",
}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
