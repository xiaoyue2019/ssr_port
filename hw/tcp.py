import requests
import json
from . import view_all

def tcp():

    url='https://ports.yougetsignal.com/check-port.php'
    ip=view_all.ip
    # ip='xx'


    post_data={
        'remoteAddress':ip,
        'portNumber':"80"
    }


    data=requests.post(url,post_data).text
    # data=data.text.encode('utf8').decode('unicode_escape')

    print(data)
    if "is closed" in data:
        return "[-]Down!"
    else:
        return "[+]TCP连接正常！"

if __name__ == "__main__":
    print(tcp())


    