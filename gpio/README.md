# Using GPIO pins on Raspberry Pi
Reference codes for controlling GPIO pins on Raspberry Pi using Python

## Installing necessary files
### Basic installation
```
sudo apt-get install python-rpi.gpio python3-rpi.gpio
sudo apt-get install python-pip python3-pip
```

## Folders
### examples
Examples include basic scripts that can be used as a reference on how to read and control the onboard GPIO pins.<br>
Additional scripts include controlling a WS2812 addressable LED strips as well as emitting keypresses. This allows GPIO-connected buttons to function like a keyboard for the Raspberry Pi.

### gpio-server
Simple experiment on using a web server hosted by Flask/Python in order to execute Python code with web requests.
