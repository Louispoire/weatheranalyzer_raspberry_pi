# weatheranalyzer_raspberry_pi
Python code used by Raspberry Pi 4 to get temperature from a DHT22 sensor and send it using POST to our service http://weatheranalyser.pythonanywhere.com/


Installation guide

Please make sure that all of theses commands have been performed on your raspberry pi

1. sudo apt update
2. sudo apt upgrade
3. sudo apt install chromium-chromedriver
4. pip3 install selenium
5. pip3 install beautifulsoup4
6. pip3 install webdriver-manager
7. pip3 install adafruit-circuitpython-dht

Now open raspberry_pi.py and run. Make sure that WebScraper.py is located in the same folder.

**If you have DHT11, please change sensor accordingly. 

Enjoy!
