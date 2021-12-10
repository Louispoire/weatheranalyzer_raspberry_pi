import adafruit_dht
import board
from datetime import date
import time
from WebScraper import WeatherScraper
import requests

# Setting up the pin
dht_device = adafruit_dht.DHT22(board.D4, False)
scraper = WeatherScraper()
# Use to calculate temperature and humidity at request
def CalculateCurrentTemperature():
    humidity = dht_device.temperature
    temperature = dht_device.humidity
    return temperature, humidity

# this method here is used to send a POST request 
def SendRequest(p):
    try:
        print("Commencing temperature transfer...")
        #meteomedia = scraper.get_current_temp_from_meteomedia()
        #weathercom = scraper.get_current_temp_from_weathercom()
        temp = { 'temp': 22, 'tempWeatherCom': 20, 'tempMeteoMedia': 20 }
        post_request = requests.post('https://weatheranalyser.pythonanywhere.com/', data=temp)
        print(post_request.text)
        
        if post_request.status_code == requests.codes.ok:
            return "OK"
        else:
            return "Bad request"
    except Exception:
        return "error"
    


while True:
    try:
        print("go")
        # Temp/Humi
        humidity = dht_device.humidity
        temperature = dht_device.temperature

        # results = precision_calculator(meteomedia, weather, temperature)
        # status = results[0]
        # precision = results[1]
        # print(status + " " + str(precision) + "%")
        if temperature == None:
            continue
        else:
            print("Temperature: " + str(temperature) + " | Humidity: " + str(humidity))
            result = SendRequest(temperature)
            if result == "error":
                print("Error. Request could not be sent")
            elif result == "Bad request":
                print("Request was sent but failed")
            elif result == "OK":
                print("Request was sucessfully sent!")
            time.sleep(5)
    except RuntimeError:
        print("Runtime error has occured. This is generally due to the sensor failing")
        continue
