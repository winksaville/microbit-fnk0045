from microbit import *
import utime

def calculate_pot_relative(adj_pot_value: int) -> int:
    assert(adj_pot_value <= BAND_SIZE)
    float_value: float = (float(adj_pot_value) / float(BAND_SIZE)) * float(ANALOG_MAX)
    int_value: int = int(float_value)
    print("calculate_pot_relative: adj_pot_vlaue: " + str(adj_pot_value) + " float_value: " + str(float_value) + " int_value: " + str(int_value))
    return int_value

UNDEFINED: int = 0
STOPPED: int = 1
FORWARD: int = 2
REVERSE: int = 3

ANALOG_MAX: int = 1023
BAND_SIZE: int = 411
STOP_REVERSE_THRESHOLD: int = BAND_SIZE
STOP_FORWARD_THRESHOLD: int = ANALOG_MAX - BAND_SIZE

motor_state: int = UNDEFINED
pot_value: int = 0
prev_pot_relative = 0

while True:
    utime.sleep(2)
    potentiometer = pin0.read_analog()
    print("potentiometer: " + str(potentiometer))
    if potentiometer <= STOP_REVERSE_THRESHOLD:
        # Motor reverse
        adj_pot_value = STOP_REVERSE_THRESHOLD - potentiometer
        pot_relative = calculate_pot_relative(adj_pot_value)
        pin2.write_digital(0)
        pin1.write_analog(pot_relative)
        pin1.set_analog_period(20)
        print("REVERSE adj_pot_value: " + str(adj_pot_value) + " pot_relative: " + str(pot_relative))
        if motor_state != REVERSE or prev_pot_relative != pot_relative:
           print("Motor REVERSE: pot_relative: " + str(pot_relative))
           motor_state = REVERSE
           prev_pot_relative = pot_relative
    elif potentiometer >= STOP_FORWARD_THRESHOLD:
        # Motor foward
        adj_pot_value = potentiometer - STOP_FORWARD_THRESHOLD
        pot_relative = calculate_pot_relative(adj_pot_value)
        pin1.write_digital(0)
        pin1.write_analog(pot_relative)
        pin2.set_analog_period(20)
        print("FORWARD adj_pot_value: " + str(adj_pot_value) + " pot_relative: " + str(pot_relative))
        if motor_state != FORWARD or prev_pot_relative != pot_relative:
            print("Motor FORWARD pot_relative: " + str(pot_relative))
            motor_state = FORWARD
            prev_pot_relative = pot_relative
    else:
        # Motor is stopped
        pin1.write_digital(1)
        pin2.write_digital(1)
        pot_relative = potentiometer - STOP_REVERSE_THRESHOLD
        print("STOPPED pot_relative: " + str(pot_relative))
        if motor_state != STOPPED or prev_pot_relative != pot_relative:
            print("Motor STOPPED: pot_relative: " + str(pot_relative))
            motor_state = STOPPED
            prev_pot_relative = pot_relative
