# Use L293D to control motor

A potentiometer is used to control the speed and direction
of the motor. The motor is stopped when the pot is
in a middle and turns in a "forward" direction faster
the farther you turn the pot to the right. If you turn
the pot to the left it will slow down then stop and
then reverse direction and go master the farther you
turn to the left.

Also the center LED is illuminated when the motor
is stopped and the left LED is dim when the motor is
"turnning" slowly in the reverse direction and brightens
the faster the motor turns. The right LED behaves the
same way for the forward directions.

# Issues

Currently the values aren't as stable as I'd like and
need to work on the filtering. But good enough for the
moment.

# Build and Run

Use `uflash`, which may require a virtual environment
```
uflash 21.2_Motor/Motor.py
```

If successful and you also attach `minicom` or other
terminal program you'll see `BAND_SIZE_TO_POT_RELATIVE`
on the terminal:
```
BAND_SIZE_TO_POT_RELATIVE: 2.489051
```

When stopped you'll see, with changing `pot_relative` values:
```
Motor STOPPED: pot_relative: 77
```

Turnning the pot left and right to turn the motor on
and turn it foward and reverse. With the pot in the
middle area it will be stopped.

Turning to the right you'll see with changing values:
```
Motor FORWARD pot_relative: 122
```

Turning to the left you'll see with changing values:
```
Motor REVERSE pot_relative: 234
```
