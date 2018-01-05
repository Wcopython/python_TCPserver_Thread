import serial.tools.list_ports
import time

plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print("没有发现端口!")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName, 38400, timeout=60)
    print("可用端口名>>>", serialFd.name)

cmd = [0x10, 0xF0, 0x00, 0x00, 0xF0, 0x16]

#serialFd.write(cmd)
#print(serialFd.readline())
#serialFd.close()
#print("串口{0:}关闭",{0:serialFd.name})
def recv(serial):
    while True:
        data =serial.read_all()
        if data ==b'':
            continue
        else:
            break
        time.sleep(0.02)
    return data
my_serial_step=0
my_count=0
while True:
    print("start serial{0:}",++my_count)
    if my_serial_step==0:
        serialFd.write(cmd)
    data =recv(serialFd)
    print(data)
    #time.sleep(5)



