# Main python
import serial
import time
import io

if __name__ == "__main__":


    ser = serial.Serial(
        port='COM3',
        baudrate=9600,
        timeout=0.1
    )

    while 1:
        string = bytes.fromhex('024203');
        ser.write(string)
        time.sleep(1)
        string = bytes.fromhex('024303');
        ser.write(string)
        print(ser.read(3).decode('utf8'))
        time.sleep(1)
