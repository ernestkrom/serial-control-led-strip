import serial

ser = serial.Serial("COM8",9600)    # Change to appropriate communication port
 
while 1:
    val = input("Mode [0-8]: ")
    ser.write(val.encode())