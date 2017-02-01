# Using GPIO pins on Raspberry Pi
Reference codes for controlling GPIO pins on Raspberry Pi using Python

## Installing necessary files
```
sudo apt-get install python-rpi.gpio python3-rpi.gpio
sudo apt-get install python-pip python3-pip

pip install python-uinput

sudo apt-get install scons
git clone https://github.com/tonydew/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python setup.py install
```

## Running
When using python-uinput module, remember to execute `sudo modprobe uinput`
