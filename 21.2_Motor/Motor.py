from microbit import *
import utime
#from builtins import *

def filter_reading(prev_value: float, cur_value: int) -> float:
    """Filter reading using EMA filter"""
    EMA_alpha: float = 0.2
    return (EMA_alpha * cur_value) + ((1 - EMA_alpha) * prev_value)

def pin0_read_analog(prev_value: float) -> float:
    """Read the analog value of pin0 and filter"""
    cv = pin0.read_analog()
    return filter_reading(prev_value, cv)

def calculate_pot_relative(adj_pot_value: int) -> int:
    assert(adj_pot_value >= 0 and adj_pot_value <= BAND_SIZE)
    # Convert to pot_relative rounding the float value up
    float_value: float = (float(adj_pot_value) * BAND_SIZE_TO_POT_RELATIVE)
    int_value: int = int(float_value + 0.5)
    #print("calculate_pot_relative: adj_pot_vlaue: " + str(adj_pot_value) + " float_value: " + str(float_value) + " int_value: " + str(int_value))
    return int_value

UNDEFINED: int = 0
STOPPED: int = 1
FORWARD: int = 2
REVERSE: int = 3

ANALOG_MAX: int = 1023
BAND_SIZE: int = 411
STOP_REVERSE_THRESHOLD: int = BAND_SIZE
STOP_FORWARD_THRESHOLD: int = ANALOG_MAX - BAND_SIZE
BAND_SIZE_TO_POT_RELATIVE: float = float(ANALOG_MAX) / float(BAND_SIZE)

motor_state: int = UNDEFINED
pot_value: int = 0
prev_pot_relative: int = 0
float_potentiometer: float = 0
prev_float_potentiometer: float = 0

print("")
print("BAND_SIZE_TO_POT_RELATIVE: " + str(BAND_SIZE_TO_POT_RELATIVE))
print("")
while True:
    utime.sleep_ms(10)
    prev_float_potentiometer = float_potentiometer
    float_potentiometer = pin0_read_analog(prev_float_potentiometer)
    potentiometer: int = int(float_potentiometer + 0.5)
    #print("potentiometer: " + str(potentiometer) + " float_potentiometer: " + str(float_potentiometer) + " prev_float_potentiometer: " + str(prev_float_potentiometer))
    if potentiometer <= STOP_REVERSE_THRESHOLD:
        # Motor reverse
        adj_pot_value = STOP_REVERSE_THRESHOLD - potentiometer
        pot_relative = calculate_pot_relative(adj_pot_value)
        pin2.write_digital(0)
        pin1.write_analog(pot_relative)
        pin1.set_analog_period(20)
        #print("REVERSE adj_pot_value: " + str(adj_pot_value) + " pot_relative: " + str(pot_relative))
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
        #print("FORWARD adj_pot_value: " + str(adj_pot_value) + " pot_relative: " + str(pot_relative))
        if motor_state != FORWARD or prev_pot_relative != pot_relative:
            print("Motor FORWARD pot_relative: " + str(pot_relative))
            motor_state = FORWARD
            prev_pot_relative = pot_relative
    else:
        # Motor is stopped
        pin1.write_digital(1)
        pin2.write_digital(1)
        pot_relative = potentiometer - STOP_REVERSE_THRESHOLD
        #print("STOPPED pot_relative: " + str(pot_relative))
        if motor_state != STOPPED or prev_pot_relative != pot_relative:
            print("Motor STOPPED: pot_relative: " + str(pot_relative))
            motor_state = STOPPED
            prev_pot_relative = pot_relative
