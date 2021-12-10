import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class WeatherScraper:
    def __init__(self):
        # create option for browser to be headless (no browser gui popup)
        ser = Service('/usr/lib/chromium-browser/chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(service=ser, options=options)

    def get_current_temp_from_meteomedia(self):
        # navigate to the meteomedia weather page
        url = "https://www.meteomedia.com/ca/meteo/quebec/montreal%22"
        self.driver.get(url)

        try:
            # wait for temperature to be visible
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, '/html/body/div[3]/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/span'))
            )

            # save the page html
            page_html = self.driver.page_source

            # Parse the page source to HTML with BeautifSulSoup
            soup = BeautifulSoup(page_html, 'html.parser')

            # Find the span element containing the current weather
            current_temp = soup.find("span", class_='temp')

            # print the result
            return float(current_temp.string)
        except:
            print("ERROR: Could not retrieve data from Meteomedia.com")
            return -1000.0

    def get_current_temp_from_weathercom(self):
        # navigate to the meteomedia weather page
        url = "https://weather.com/en-CA/weather/today/l/623267a6cbae200f3c71ffba3e29de9696db705ae363efd10c32b3072fa43af4"
        self.driver.get(url)

        try:
            # wait for temperature to be visible
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, '/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[2]/div[1]/span'))
            )

            # save the page html
            page_html = self.driver.page_source

            # Parse the page source to HTML with BeautifulSoup
            soup = BeautifulSoup(page_html, 'html.parser')

            # Find the span element containing the current weather
            current_temp = soup.find("span", class_='CurrentConditions--tempValue--3a50n')

            # print the result
            return float(current_temp.string.replace('°', ''))
        except:
            print("ERROR: Could not retrieve data from Weather.com")
            return -1000.0

