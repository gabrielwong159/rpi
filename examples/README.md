## arduino_serial
Communicating via Arduino USB Serial

## azure_sql
Accessing Azure hosted SQL server using PyODBC
```sudo apt-get install freetds-dev freetds-bin unixodbc-dev tdsodbc
pip install pyodbc```

In ```/etc/odbcinst.ini```:
```[FreeTDS]
Description=FreeTDS Driver
Driver=/usr/lib/arm-linux-gnueabihf/odbc/libtdsodbc.so
Setup=/usr/lib/arm-linux-gnueabihf/odbc/libtdsS.so```
[Source](https://gist.github.com/rduplain/1293636)

## blink_led
Simple single LED blink

## button_control
Program for button-toggled LED

## button_test
Prints "YES" while button held down, "NO" otherwise

## nanpy_fade
Using the [Nanpy](https://github.com/nanpy/nanpy) library for Arduino

## neopixel_demo
Simple example on how to use NeoPixel library in RPi

## uinput_test
Simple example on how to use button input to emit keypresses in RPi
