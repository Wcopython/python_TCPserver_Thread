import socket
import  datetime

################################333
x=0
while True:
        sk = socket.socket()
        #sk.bind(("106.14.41.25",2216))
        sk.bind(("127.0.0.1",2216))
        sk.listen(5)
        conn,address = sk.accept()
        x=x+1
        myls="hello world="+str(x)
        conn.sendall(bytes(myls,encoding="utf-8"))
        my_all_step=0
        my_heart_time_count=1
        try:
            while True:
                buf=conn.recv(1024)
                print(buf)
                #conn.close()
                #sk.close()
                print("tcp get data")
                break
        finally:
            print("ERROR")
            pass
