import requests
import json
from . import view_all

def ping():

    url='https://www.wepcc.com/check-ping.html'
    ip=view_all.ip
    # ip='xx'

    post_data={
        'node':'1',
        'host':ip
    }


    data=requests.post(url,post_data)
    data=data.text.encode('utf8').decode('unicode_escape')

    print(data)
    if "超时" in data:
        return "[-]Timeout!"
    else:
        return "[+]ping检测成功！主机在线！"

if __name__ == "__main__":
    print(ping())