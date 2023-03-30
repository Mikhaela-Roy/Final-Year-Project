import serial

arduino = serial.Serial('COM6', 9600)

data = []

while True:
    cmd = str(input('enter command: '))
    cmd = cmd + '\r'
    arduino.write(cmd.encode())

