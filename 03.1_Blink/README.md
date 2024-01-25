# 03.1_Blink

This blinks the middle LED on the microbit as well as an
LED if it's attached to pin0 of the GPIO board.

Plug in the microbit and start two terminals.

In one terminal start minicom:
```
Welcome to minicom 2.9

OPTIONS: I18n
Compiled on Sep 23 2023, 19:55:08.
Port /dev/ttyACM0, 11:58:40

Press CTRL-A Z for help on special keys
```


In the other terminal flash the Blink.py program to the microbit:
```
uflash Blink.py
```

When the program starts running in the microbit
terminal you should see `Counter: X bit0: Y` and
also the LEDs should be blinking. Press `CTRL-C`
and you'llsee the Traceback and KeyboardInterrupt:
```
Counter: 0 bit0: 0

Counter: 1 bit0: 1

Counter: 2 bit0: 0

Counter: 3 bit0: 1

Counter: 4 bit0: 0

Traceback (most recent call last):

  File "main.py", line 13, in <module>

KeyboardInterrupt:

MicroPython v1.13 on 2021-03-16; micro:bit v2.0.0-beta.5 with nRF52833

Type "help()" for more information.

>>> 
```