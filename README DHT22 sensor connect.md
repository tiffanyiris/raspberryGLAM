# MMM-Temperature-Humidity
Temperature and Humidity monitoring Module for MagicMirror<sup>2</sup>
This module works for DHT11, DHT22 and AM2302 sensors.

## Dependencies
  * An installation of [MagicMirror<sup>2</sup>](https://github.com/MichMich/MagicMirror)
  * npm
  * [rpi-dht-sensor](https://www.npmjs.com/package/rpi-dht-sensor)

## Installation
 1. Clone this repo into `~/MagicMirror/modules` directory.
 2. Configure your in `~/MagicMirror/config/config.js`:

    ```
    {
        module: 'MMM-Temperature-Humidity',
        position: 'top_right',
        config: {
            ...
        }
    }
    ```
 3. Run command `npm install` in `~/MagicMirror/modules/MMM-STT` directory.
 4. Run command `sudo apt-get install rpi-dht-sensor`.
 5. sudo npm start in `~/MagicMirror`.

## Config Options
| **Option** | **Default** | **Description** |
| --- | --- | --- |
| `refreshInterval` | `50000` | Time in milli seconds before successive readings are taken. |
| `temperaturePrefix` | `'Room temperature: '` | Text to display as prefix of Temperature Reading |
| `temperatureSuffix` | `'°C'` | Text to display as suffix of Temperature Reading |
| `humidityPrefix` | `'Humidity: '` | Text to display as prefix of Humidity Reading |
| `humiditySuffix` | `'%'` | Text to display as suffix of Humidity Reading |


# Connecting DHT22 Sensor to Raspberry Pi 4B

This guide will help you connect a DHT22 (AM2302) sensor to a Raspberry Pi 4B and read temperature and humidity data using Python.

## Requirements

- Raspberry Pi 4B with Raspbian OS installed
- DHT22 (AM2302) sensor
- Female-to-male jumper wires (3-4 wires)
- Breadboard (optional)

## Steps

### Step 1: Gather Your Components

Ensure you have all the necessary components ready:

- Raspberry Pi 4B with Raspbian OS installed
- DHT22 (AM2302) sensor
- Female-to-male jumper wires (3-4 wires)
- Breadboard (optional)

### Step 2: Identify DHT22 Pins

Identify the pins on your DHT22 sensor. It typically has four pins:

- VCC (Power): Connects to 3.3V on the Raspberry Pi.
- Data: Connects to a GPIO pin on the Raspberry Pi.
- NC (Not Connected): Leave this pin unconnected.
- GND (Ground): Connects to a ground pin on the Raspberry Pi.

### Step 3: Connect the DHT22 to the Raspberry Pi

a. Connect the VCC pin on the DHT22 to the 3.3V pin on the Raspberry Pi.
b. Connect the Data pin on the DHT22 to a GPIO pin on the Raspberry Pi. Choose any GPIO pin, but remember the pin number for software configuration.
c. Connect the GND pin on the DHT22 to a ground (GND) pin on the Raspberry Pi.

If you're using a breadboard, you can connect the DHT22 sensor and Raspberry Pi GPIO pins on the breadboard to keep the connections organized.

### Step 4: Install Required Libraries

Before you can read data from the DHT22 sensor, you'll need to install the necessary libraries. Open a terminal on your Raspberry Pi and run the following commands:

```bash
sudo apt-get update
sudo apt-get install python3-dev python3-pip
sudo pip3 install Adafruit_DHT

Step 5: Test the Sensor
Create a new Python script (e.g., dht22_sensor.py) and use code similar to the example provided in the dht22_sensor.py file in this repository. Save the script.

Run the script using the following command: python3 dht22_sensor.py

You should see temperature and humidity data printed to the terminal.
