# Using GPIO pins on Raspberry Pi
Reference codes for controlling GPIO pins on Raspberry Pi using Python

## Installing necessary files
```
sudo apt-get install python-rpi.gpio python3-rpi.gpio
sudo apt-get install python-pip python3-pip

pip install python-uinput

sudo apt-get install scons swig
git clone https://github.com/tonydew/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python setup.py install
```

## Running
When using python-uinput module, remember to execute `sudo modprobe uinput`

If the NeoPixels do not respond well to commands (i.e. funny random colours), the PWM might possibly be affected by the audio driver. Create a file ```/etc/modprobe.d/snd-blacklist.conf``` and add the line `blacklist snd_bcm2835`
