import requests
import json

d = {"text":"hello", "author":"world"}
print(d)
requests.post('http://127.0.0.1:5000/newquote', json=d)