from microbit import *
import utime


def filter_reading(prev_value: int, cur_value: int) -> int:
    """Filter reading using EMA filter"""
    EMA_alpha: float = 0.6
    return (EMA_alpha * cur_value) + ((1 - EMA_alpha) * prev_value)

def pin0_read_analog(prev_value: int) -> int:
    """Read the analog value of pin0 and filter"""
    cv = pin0.read_analog()
    return filter_reading(prev_value, cv)

def round_up(x: float) -> int:
    """Round up a float to the nearest integer"""
    return int(x + 0.5)

# Trigger to update pin1
diff_fuzz = 1.0

# Clamp pot_value to 0 if diff is >= diff_clamp_to_0
diff_clamp_to_0 = 0.01

# Read pot_value and make prev_pot_value different
# so the first time through the loop we'll always
# write a new value.
pot_value: float = pin0_read_analog(0)
pot_value_int = round_up(pot_value)
prev_pot_value: float = pot_value + diff_fuzz;

print("initial pot_value: " + str(pot_value) + " " + str(pot_value_int) +
      " prev_pot_value: " + str(prev_pot_value))

## Loop updating pin1 if pin0 changed we do this
counter: int = 0
while True:
    counter = counter + 1
    diff: float = abs(prev_pot_value - pot_value)

    # If the difference is greater than the diff_fuzz or
    # the pot_value_int is 0 and diff is >= diff_clamp_to_0
    # then we clamp at 0 otherwise sometimes we won't zero.
    if (diff >= diff_fuzz) or ((pot_value_int == 0) and (diff >= diff_clamp_to_0)):
        # It's different so update pin1 and tell the user
        pin1.write_analog(pot_value_int)
        print("counter: " + str(counter) +
              " pot_value: " + str(pot_value) + " " + str(pot_value_int) +
              " prev_pot_value: " + str(prev_pot_value) +
              " diff: " + str(diff))

    # Read new value, may or may not be different
    prev_pot_value = pot_value
    pot_value = pin0_read_analog(prev_pot_value)
    pot_value_int = round_up(pot_value)

    # This slight delay improves the smoothness around 0
    # not sure why but it does.
    utime.sleep_ms(50)
