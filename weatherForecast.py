"""
    This is a simple program to get the weather forecast report from Google.

    The program will use the BeautifulSoap library that is used to make screen-scraping, and the requests module that helps to integrate the Python programs with the web services.

    To install beautifulsoup use the following command: pip install beautifulsoup

    To install requests use the following command: pip install requests
"""

from bs4 import BeautifulSoup
import requests


# Setting the User-Agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Function to get the weather information
def weather(city):
    city = city.replace(" ", "+")
    # Requesting information from the URL
    res=requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0. i635i39l2j0l4j46j690.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)

    print("\nBuscando en Google...\n")

    # BeautifulSoup to navigate the website and extract the data and store it in soup object
    soup = BeautifulSoup(res.text,'html.parser')

    # This is the code to extract the information about location, time, info, weather, etc.
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    humidity = soup.select('#wob_hm')[0].getText().strip()
    windSpeed = soup.select("#wob_ws")[0].getText().strip()
    probPrecip = soup.select("#wob_pp")[0].getText().strip()

    print("*" * 35)
    print("Ciudad:              " + location)
    print("Fecha Actualización: " + time)
    print("Estado del Clima:    " + info)
    print("Temperatura:         " + weather + " °C")
    print("Humedad:             " + humidity)
    print("Velocidad Viento:    " + windSpeed)
    print("Probabilidad Lluvia: " + probPrecip)
    print("*" * 35)


print("")
print("*" * 35)
print("       Información del clima")
print("*" * 35)
print("\nIngrese el nombre de la ciudad: ")
print("")
city = input()

city = city + "weather"

weather(city)
print("")
