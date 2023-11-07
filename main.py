import os
import time
import datetime
from pythonping import ping


def check_online(ip: str):
    message = ping(ip)
    print(message)
    success_ping = "Reply"
    if success_ping in str(message):
        success_flg = 1
    else:
        success_flg = 0
    return success_flg


file = 'Ping_Log.txt'
network_dead_flg = 1
_response = 1
with open(file, "a", encoding='utf-8') as f:
    while(network_dead_flg):
        response = check_online('104.193.88.77')
        if response != 1:
            if _response:
                time_start = time.time()
            time_now = time.time()
            time_str = datetime.datetime.fromtimestamp(time_now).strftime("%Y-%m-%d %H:%M:%S")
            log_text = '\n Connection lost at ' + time_str
            f.write(log_text)
            if time_now - time_start > 300:
                network_dead_flg = 0
                log_text = '\n Connection lost over 5 minutes, detection stop'
                f.write(log_text)
            _response = response

