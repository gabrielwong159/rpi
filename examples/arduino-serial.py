import serial
ser = serial.Serial("/dev/ttyUSB0", 9600)

while True:
    # when the Arduino sends an entire string i.e. Serial.println("Hello, World!")
    # Python is able to read the entire string
    print(ser.readline().strip())

# when sending multiple characters
# Arduino will parse all of the above
ser.write('0123')

# i.e.
# if (Serial.available()) {
#     int value = (int)(Serial.read()-'0');
#     strip.setPixelColor(value,255,0,0);
#     strip.show();
# }
#
# will show all 4 pixels
