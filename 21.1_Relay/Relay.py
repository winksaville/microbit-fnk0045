# Button A turns motor ON Button B turns it OFF
from microbit import *

OFF: int = 0
ON: int = 1

# Set initial conditions
print("Starting with motor off");
motor_state: int = OFF
pin0.write_digital(motor_state)

# Loop changing motor state when buttons are pressed
while True:
    if button_a.is_pressed() and motor_state == OFF:
        print("Motor is on")
        motor_state = ON
        pin0.write_digital(motor_state)
        display.set_pixel(2, 2, 9)
    elif button_b.is_pressed() and motor_state == ON:
        print("Motor is off")
        motor_state = OFF
        pin0.write_digital(motor_state)
        display.set_pixel(2, 2, 0)

