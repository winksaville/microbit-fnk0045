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

def print_info(extra: str):
        print("counter: " + str(counter) +
              " pot_value: " + str(pot_value) + " " + str(pot_value_int) +
              " prev_pot_value: " + str(prev_pot_value) +
              " diff: " + str(diff) +
              " " + extra)

def update_next_info_time():
    global next_info_time
    next_info_time = utime.ticks_add(utime.ticks_ms(), info_threshold)

def is_next_info_time() -> bool:
    if utime.ticks_diff(next_info_time, utime.ticks_ms()) <= 0:
        update_next_info_time()
        return True
    else:
        return False

# Trigger to update pin1
diff_fuzz: float = 1.0

# Zero threshold
zero_threshold: float = 0.8

# Read pot_value and make prev_pot_value different
# so the first time through the loop we'll always
# write a new value.
pot_value: float = pin0_read_analog(0)
pot_value_int = round_up(pot_value)
prev_pot_value: float = pot_value + (diff_fuzz * 2);
diff: float = 0.0
counter: int = 0
info_threshold: int = 3000
next_info_time: int = update_next_info_time()
loop_delay_ms: int = 10

print_info("Initial")

## Loop updating pin1 if pin0 changed we do this
while True:
    counter = counter + 1
    diff: float = abs(prev_pot_value - pot_value)

    # Every few seconds output the info
    if is_next_info_time():
        print_info("info @ " + str(utime.ticks_ms()))

    # The pot can be flaky and not actually get to zero
    # so we'll fake if it's below zero_threshold.
    if (pot_value < zero_threshold) and (prev_pot_value != 0):
        pin1.write_analog(0)
        print_info("Clamp to 0")

        # Set previous value to 0 as we've forced it
        prev_pot_value = 0

    # If the difference is greater than the diff_fuzz or
    if (diff > diff_fuzz):
        pin1.write_analog(pot_value_int)
        print_info("diff > diff_fuzz")

        # Save as previous value
        prev_pot_value = pot_value

    # Read new value, may or may not be different
    pot_value = pin0_read_analog(prev_pot_value)
    pot_value_int = round_up(pot_value)

    # Previously this made things "smoother", not sure why,
    # but now maybe this might reduce power consumption, at
    # least that's possible. Of course more delay make it less
    # responsive.
    if loop_delay_ms > 0:
        utime.sleep_ms(loop_delay_ms)
