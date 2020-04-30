import serial
import time
from threading import Thread, Timer
import os


a1=100
a2=200
a3=300
a4=400
isTracking=1

time_t=0.05
t=0

ser = serial.Serial(
    port = 'COM8',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
)

next_call = time.time()


def send_serial():
    global a1, a2, a3, a4, isTracking, next_call, time_t, t
    

    dataa1=a1.to_bytes(2, byteorder = "little", signed = True)
    a1L=dataa1[1]
    a1H=dataa1[0]
    dataa2=a2.to_bytes(2, byteorder = "little", signed = True)
    a2L=dataa2[1]
    a2H=dataa2[0]
    dataa3=a3.to_bytes(2, byteorder = "little", signed = True)
    a3L=dataa3[1]
    a3H=dataa3[0]
    dataa4=a4.to_bytes(2, byteorder = "little", signed = True)
    a4L=dataa4[1]
    a4H=dataa4[0]

    dataIsTracking=isTracking

    packet = [dataIsTracking, a1L, a1H, a2L, a2H, a3L, a3H, a4L, a4H]
    print(packet)
    print("{} * {} * {} * {} \n".format(a1, a2, a3, a4))
    #print("time: ",time.time())
    # packet = [chr(dataIsTracking), chr(dataX1), chr(dataX2), chr(dataY1), chr(dataY2)]
    # print("{} - - {}".format(packet, type(packet)))
    ser.write(packet)
    t+=1
    
    next_call = next_call + time_t
    Timer( next_call - time.time(), send_serial ).start()

send_serial()

def main():
    global a1, a2, a3, a4, isTracking

    x = 2
    y = -2
    while True:
        a1 = a1+x
        a2 = a2+x+1
        a3 = a3+x-1
        a4 = a4+x-2
        if (a1>=250):
            x = -2
        elif (a1<=100):
            x = 2
        time.sleep(0.1)

if __name__ == '__main__':
    main()
    print("start....")
