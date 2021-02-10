import time
import os
import json
import math
import requests
from urllib.parse import urljoin, urlencode, quote, quote_plus

from fritzconnection.lib.fritzstatus import FritzStatus

print("Starting up...")

model_id = os.getenv('MODEL_ID', "ctron.fritzbox.status:1.0.0")

app_id = os.getenv('APP_ID')
device_id = quote(os.environ['DEVICE_ID'])
device_password = os.getenv('DEVICE_PASSWORD')

endpoint = os.environ['ENDPOINT']
print(endpoint)

denc = quote_plus(device_id)
auth = (f"{denc}@{app_id}", device_password)

path = f"/v1/status"
query = "?" + urlencode(dict(model_id=model_id))
url = urljoin(endpoint, path + query)

print(url)

fc = FritzStatus(password=os.environ['PASSWORD'])
while True:
    t = fc.transmission_rate
    status = {
        "timestamp": math.trunc(time.time() * 1000.0),
        "rate_send": t[0],
        "rate_receive": t[1],
        "bytes_received": fc.bytes_received,
        "bytes_sent": fc.bytes_sent
    }
    print(json.dumps(status))
    res = requests.post(url, json=status, auth=auth, headers={"Content-Type": "application/json"})
    print(res)

    time.sleep(2)
