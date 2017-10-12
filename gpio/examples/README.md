## [neopixel_demo](https://github.com/tonydew/rpi_ws281x)
Simple example on how to use NeoPixel library in RPi

### Installation
```
sudo apt-get install scons swig
git clone https://github.com/tonydew/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python setup.py install
```

## [uinput_test](https://github.com/tuomasjjrasanen/python-uinput)
Simple example on how to use button input to emit keypresses in RPi

### Installation
```
pip install python-uinput
```

### Running
When using python-uinput module, remember to execute `sudo modprobe uinput`

If the NeoPixels do not respond well to commands (i.e. funny random colours), the PWM might possibly be affected by the audio driver. Create a file ```/etc/modprobe.d/snd-blacklist.conf``` and add the line `blacklist snd_bcm2835`
