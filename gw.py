import thingspeak
import serial
import time


# Serial USB parameters
SERIAL_PORT = "COM10"
BAUD_RATE = 9600
ser = serial.Serial(SERIAL_PORT, baudrate=BAUD_RATE)

# Thingspeak parameters
# https://thingspeak.readthedocs.io/en/latest/api.html
channel_id = 0000000
write_key = ""
channel = thingspeak.Channel(id=channel_id, api_key=write_key)


while True:
    # Read serial data : #temperature,humidity
    raw_sensor = ser.readline().strip().decode()
    if raw_sensor[0] == '#':
        sensors_data = raw_sensor.split('#')[1]
        humidity = sensors_data.split(',')[0]
        temperature = sensors_data.split(',')[1]
    else:
        print('Error getting Arduino sensor values over serial')
        continue

    # Send data to Thingspeak platform
    data = {1: humidity, 2: temperature}
    response = channel.update(data)
    print(response)

    # Pause
    time.sleep(1)

