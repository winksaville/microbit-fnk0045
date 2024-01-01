from microbit import *

readings = [pin0.read_analog()] * 50
readings_index: int = 0
sum_readings: int = 0
avg_as_float: float = 0.0
av_round_up: float = 0.0
cv: int = 0
av: int = 0

def print_readings():
    """Print the current readings   """
    global readings_index, readings, cv, av, av_round, sum_readings
    print("readings_index: " + str(readings_index) +
          " cv: " + str(cv) +
          " sum: " + str(sum_readings) +
          " avg_as_float: " + str(avg_as_float) +
          " av_round_up: " + str(av_round_up) +
          " av: " + str(av) +
          " readings: " + str(readings))

def pin0_read_analog() -> int:
    """Read the analog value of pin0
    filter it with a moving average filter.
    This is "OK" but not great it will still
    wonder around a bit."""
    global readings_index, readings, sum_readings, cv, av, av_round_up, avg_as_float

    # Read the current value
    cv = pin0.read_analog()

    # Update the readings array
    readings[readings_index] = cv

    # increment the index and wrap around
    readings_index = (readings_index + 1) % len(readings)

    # Sum the readings
    sum_readings = sum(readings)

    # Calculate the average, which is a float
    avg_as_float = sum_readings / len(readings)

    # Round up by 0.5
    av_round_up = avg_as_float + 0.5

    # Truncate to an int
    av = int(av_round_up)

    # return the average integer value
    return av
    
# Read pot_value and make prev_pot_value different
# so the first time through the loop we'll always
# write a new value.
pot_value: int = pin0_read_analog()
prev_pot_value: int = pot_value + 1
print("initial pot_value: " + str(pot_value) +
      " prev_pot_value: " + str(prev_pot_value))

## Loop updating pin1 if pin0 changed we do this
counter: int = 0
while True:
    counter = counter + 1
    if prev_pot_value != pot_value:
        # It's different so update pin1 and tell the user
        pin1.write_analog(pot_value)
        print("counter: " + str(counter) + " pot_value: " + str(pot_value))
        print_readings()

        # Update prev_pot_value so we can detect changes
        prev_pot_value = pot_value

    # Read new value, may or may not be different
    pot_value = pin0_read_analog()
