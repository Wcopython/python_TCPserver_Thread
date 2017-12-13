#多线程TCP服务器端
import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):

        conn = self.request
        myls=bytes((0x01,0x02,0x03))

        conn.sendall(myls)

        Flag = True

        while Flag:

            data = conn.recv(1024)
            print(data)

            if data == 'exit':

                Flag = False

            elif data == '0':

                conn.sendall(b"abc")

            else:

                conn.sendall(b"123")

if __name__ == '__main__':

    server = socketserver.ThreadingTCPServer(('127.0.0.1',2216),MyServer)

    server.serve_forever()