from microbit import *

# Blink an led connected to pin0
counter: int = 0
while True:
    bit0: int = counter & 1
    print("Counter: " + str(counter) + " bit0: " + str(bit0))
    pin0.write_digital(bit0)
    sleep(500)
    counter = counter + 1
