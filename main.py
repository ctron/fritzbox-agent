import time
import os
import json
import math
import requests
from urllib.parse import urljoin, urlencode, quote

from fritzconnection.lib.fritzstatus import FritzStatus

model_id = os.getenv('MODEL_ID', "ctron.fritzbox.status:1.0.0")
device_id = quote(os.environ['DEVICE_ID'])

endpoint = os.environ['ENDPOINT']
path = f"/publish/{device_id}/status"
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
    res = requests.post(url, json=status, headers={"Content-Type": "application/json"})
    print(res)

    time.sleep(2)
