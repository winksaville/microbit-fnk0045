from microbit import *
import utime

# Test we can use print to output to the serial port
loop_number: int = 0
while True:
    loop_number = loop_number + 1
    print("loop_number: " + str(loop_number))
    sleep(1000)
