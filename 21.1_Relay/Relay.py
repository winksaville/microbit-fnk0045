# Turn on the motor when Button A is pressed
from microbit import *

OFF: int = 0
ON: int = 1

# Set initial conditions
print("Starting with motor off");
motor_state: int = OFF
pin0.write_digital(motor_state)

# Loop changing motor state when button is pressed or released
while True:
    if button_a.is_pressed() and motor_state == OFF:
        print("Motor is on")
        motor_state = ON
        pin0.write_digital(motor_state)
        display.set_pixel(2, 2, 9)
    elif button_a.is_pressed() == False and motor_state == ON:
        print("Motor is off")
        motor_state = OFF
        pin0.write_digital(motor_state)
        display.set_pixel(2, 2, 0)

