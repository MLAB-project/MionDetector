import serial
import time

# Nastavení sériového portu
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def read_serial():
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)

try:
    print("Reading data from serial port...")
    read_serial()
except KeyboardInterrupt:
    print("Exiting program.")
finally:
    ser.close()

