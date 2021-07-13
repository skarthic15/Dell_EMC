"""
Create Python REST client program which queries http://api.open-notify.org/astros.json and list the user name in sorted order.
Convert the REST JSON object to list<String> with JSON names in sorted order. (python)
"""
import requests

url = "http://api.open-notify.org/astros.json"

# Connect url and get the output in json
conn = requests.get(url)
out = conn.json()

# Get userlist and sort
res = sorted([i['name'] for i in out['people']])
print(res)


