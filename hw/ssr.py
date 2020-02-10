import base64
import MySQLdb as mdb
from . import view_all



def main():
    port='65535'
    pwd='cnmf.net.cn'
    group=''
    con = None
    ip=view_all.ip
    
    try:
        con = mdb.connect('127.0.0.1', 'root','xx', 'test')
        cur = con.cursor()
        cur.execute("select * from xx")
        data = cur.fetchall()
        port=data[-1][1].replace('\n','')
        print(port)
    finally:
        if con:
            con.close()

    ssr=ip+':'+port+':auth_sha1_v4:aes-192-cfb:http_simple:'+base64.b64encode(pwd.encode()).decode().replace('=','')+'/?obfsparam=&group='+base64.b64encode(group.encode()).decode()



    print(ssr)
    #xx


    def _encode(s):
        _t1=base64.b64encode(s.encode())
        _t2=base64.b64encode(b'ssr://'+_t1).decode()
        print(_t2)
        return _t2



    def _deocde(s):
        return base64.b64decode(s).decode()


    with open('C:/xampp/htdocs/xx.html','w') as f:
        f.write(_encode(ssr))

if __name__ == "__main__":
    main()

 