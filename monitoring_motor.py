import serial

arduino = serial.Serial('COM6', 9600)

data = []

while True:
    cmd = str(input('enter command: '))
    cmd = cmd + '\r'
    arduino.write(cmd.encode())

##def retrieve():
##    arduino.write(b'1')
##    data = arduino.readline().decode('acsii')
##    return data
##
##while True:
##    dat = input("Retrieve data? ")
##    if dat == '1':
##        print(retrieve())
##    else:
##        arduino.write(b'0')
