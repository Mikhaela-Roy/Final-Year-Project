import serial
import time

arduino = serial.Serial('COM6', 9600)

data = []

while True:
    cmd = input('enter command: ')
    cmd = cmd + '\r'
    arduino.write(cmd.encode())

arduino.close()
