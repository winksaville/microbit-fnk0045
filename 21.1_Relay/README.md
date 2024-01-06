# Turn a motor on/off using button A

When the MicroBit is attached to the Freenove
GPIO Extension Board and it's attached to the
circut described in Chapter 21.1 of the FNK0045
Tutorial this code turns the motor on and off.

In addition the code turns on the center LED of the
MicroBit display when the motor is ON. This allows
the program logic to be tested without the circut
board being attached.

# Build and Run

Use `uflash`, which may require a virtual environment
```
uflash 21.1_Relay/Relay.py
```

If successful and you also attach `minicom` or other
terminal program you'll see `Starting with motor off`
on the terminal:
```
Starting with motor off
```

Pressing Button A on the MicroBit board will
turn on the motor and `Motor is on` is added to the
serial port output:
```
Starting with motor off
Motor is on
```

Pressing Button B `Motor is off` is added:
```
Starting with motor off
Motor is on
Motor is off
```

# Notes

Pressing Button A/B quickly sometimes causes the
program to start from the beginning!
```
Starting with motor off
Motor is on
Motor is off
Starting with motor off
Motor is on
Motor is off
Motor is on
Motor is off
Motor is on
Motor is off
Starting with motor off
Motor is on
Motor is off
```

I'm not sure why but if I remove the connections to the circuit
board and then press Button A quickly it does not happen. That
would lead me to believe something is wrong with the circuit
design or my implementation. My guess is the "Back EMF" from the
relay is causing the problem.
```
Starting with motor off
Motor is on
Motor is off
Motor is on
Motor is off
Motor is on
Motor is off
Motor is on
Motor is off
Motor is on
Motor is off
Motor is on
Motor is off
Motor is on
Motor is off
Motor is on
Motor is off
Motor is on
Motor is off
Motor is on
Motor is off
```

