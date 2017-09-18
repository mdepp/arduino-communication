"""
Tests some basic communication between Arduino and program
"""
import serial
import msvcrt
import sys

try:
    port_name = sys.argv[1] if len(sys.argv) > 1 else 'COM3'

    with serial.Serial(port_name, 9600, timeout=0) as ser:
        print('Serial port:', ser.name)
        while True:
            byte_read = ser.read()
            if byte_read:
                print(byte_read.decode('ascii', errors='ignore'), end='', flush=True)

            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b'\x03':
                    break

                if key == b'\r':
                    data = b'\r\n'
                elif key == b'\b':
                    data = b'\b \b'
                else:
                    data = key
                
                ser.write(data)

except Exception as e:
    print(e)
except:
    print('Exception caught.')
