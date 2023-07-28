# RaspberryGLAM


##  Hardware Setup
###  Setting up the TouchScreen:
1.  Use the long ribbon cable and connect it blue side down to the touchscreen in the port on the left side.
    a. To connect it, carefully pull up on the black plastic piece (the catch) on the bottom of the port, and then slide the ribbon cable in (blue side down)
    b. To finish inserting the ribbon, secure the catch by carefully pushing it back in.  You should hear a small click noise.  Be careful as it does take a bit of pressure to secure the catch, make sure not to bend the ribbon cable.
2.  Connect the ribbon cable to the display port in the raspberry pi, following instructions 1a and 1b. 

Optionally, you may align the 4 holes in the corners of the pi and screw them into the touchscreen to secure it
See the picture below.  There are 5 pins on the bottom board, which is the touchscreen, insert the 4 cables into the pins, skipping the second from the right.  

![PXL_20230714_173846358](https://github.com/tiffanymeow/raspberryGLAM/assets/57841282/49669860-83ae-44ae-ab47-991ba0255fbd)

Connect the wires to the pi pins above as shown.  See raspberry pi pin numbering picture below.

The red wire connects to the 5V power pin, #4 on the diagram. 
The green wire connects to GPIO 2, #3 on the diagram
The yellow wire connects to GPIO 3, #5 on the diagram
The black wire connect to Ground, #6 on the diagram

![GPIO](https://github.com/tiffanymeow/raspberryGLAM/assets/57841282/c5a65f32-be13-4ea4-b2ac-a8d1d0bfe7ce)

###  Setting up the Sensor:
The wire connected to the plus, the leftmost wire, connects to the 3v3 power at pin #17
The middle wire connects to GPIO 22, directly above it #15
The minus wire, or the rightmost wire connects to the ground pin, #20

![PXL_20230714_173857459](https://github.com/tiffanymeow/raspberryGLAM/assets/57841282/13aca788-d7ba-48fb-bd81-328bd749870b)

###  Connecting the Camera

The camera is relatively simple to connect, as there is only one ribbon cable needed.  Simply insert the ribbon cable blue side down into the camera and secure the catch.  Do the same to the port marker 'Camera' on the Raspberry Pi.  The blue side should be oriented facing the keyboard and mouse USB ports.  

##  Magic Mirror

See the [Magic Mirror website] for further documentation: (https://magicmirror.builders/)

##  Temperature and Humidity Alert
You will need to install the driver for the sensor.
``` pip3 install adafruit-circuitpython-dht```

Download the sensor.py file to your raspberry pi.  You will then need to create a new virtual enviornment with the following commands:

```
mkdir project-name && cd project-name
python3 -m venv .venv
source .venv/bin/activate
pip3 install adafruit-circuitpython-dht

```


##  Facial Recognition

