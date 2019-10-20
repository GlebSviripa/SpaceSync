import time
import requests

url = "https://webpad.com.ua/servo"
r = requests.post(url)
print(r.status_code, r.reason, r.text)

result = r.text

