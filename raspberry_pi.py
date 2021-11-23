import adafruit_dht
import board
from datetime import date
import time
from TemperatureValidator import *
import requests

# Setting up the pin
dht_device = adafruit_dht.DHT22(board.D4, False)


# Use to calculate temperature and humidity at request
def CalculateCurrentTemperature():
    humidity = dht_device.temperature
    temperature = dht_device.humidity
    return temperature, humidity


meteomedia = 25
weather = 26

while True:
    test_file = open('test.txt', 'a')
    try:
        # Temp/Humi
        humidity = dht_device.humidity
        temperature = dht_device.temperature

        # day/month/time
        this_day = date.today()
        this_month = date.month()
        t = time.localtime()
        this.time = time.strftime("%H:%M", t)

        print(this_day + " " + this_month + " " + this.time)

        results = precision_calculator(meteomedia, weather, temperature)
        status = results[0]
        precision = results[1]
        print("Temperature: " + str(temperature) + " | Humidity: " + str(humidity))
        print(status + " " + str(precision) + "%")
        test_file.write(
            "Temperature: " + str(temperature) + " | Humidity: " + str(humidity) + " | " + status + " " + str(
                precision) + "%\n")

        sendRequest(temperature)
        time.sleep(5)
    except RuntimeError:
        print("Runtime error has occured. This is generally due to the sensor failing")
        continue


def SendRequest(temperature):
    temp = {'temp': temperature}
    post_request = requests.post('uri', data=temp)

    if post_request.status_code = requests.codes.ok:
        print("nice")



