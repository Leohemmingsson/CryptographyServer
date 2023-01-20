import requests

url = "http://127.0.0.1:5000" + "/make_file"

# post json to url
data = {
    "type": "AC17",
    "data": "This is the data",
    "attributes": {"area": "testing", "access": 2},
}
response = requests.post(url, json=data)
print(response.status_code)
