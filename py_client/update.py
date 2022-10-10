import requests
endpoint = "http://127.0.0.1:8000/api/products/1/update/"

data={
    "title": "Happy to be here",
    "price": 129.99,
    "my_discount": 4.99
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())
