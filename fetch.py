from bs4 import BeautifulSoup
import requests

r = requests.get("https://ndbc.noaa.gov/activestations.xml")
soup = BeautifulSoup(r.text)
buoy_soup = soup.find_all(type="buoy")
print(len(buoy_soup))
