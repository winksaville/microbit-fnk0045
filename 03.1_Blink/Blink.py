from microbit import *

# Blink an led connected to pin0
counter: int = 0
while True:
    bit0: int = counter & 1
    print("Counter: " + str(counter) + " bit0: " + str(bit0))

    # Write to pin0 to toggle the LED attached to the GPIO board
    pin0.write_digital(bit0)

    # Write to the middle pixel also, incase the GPIO board is not attached
    if bit0 == 0:
        display.set_pixel(2, 2, 0)
    else:
        display.set_pixel(2, 2, 9)

    # Sleep for 500ms
    sleep(500)

    counter = counter + 1
