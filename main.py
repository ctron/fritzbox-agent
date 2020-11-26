import time
import os
import json
import math

from fritzconnection.lib.fritzstatus import FritzStatus

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
    time.sleep(2)
