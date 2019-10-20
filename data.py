from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageTk


class FilteredXML:
    def __init__(self, xml):
        self.elev = xml.get("elev")
        self.lat = xml.get("lat")
        self.lon = xml.get("lon")
        self.owner = xml.get("owner")
        self.name = xml.get("name")


class Map:
    def __init__(self, image_path, buoys):
        self.image = Image.open(image_path)
        self.image_ref = ImageTk.PhotoImage(self.image)
        self.width = self.image.width
        self.height = self.image.height
        self.offset = self.image.width / 4
        self.buoys = buoys


class BuoyPoint:
    def __init__(self, buoy_xml, map_object):
        self.buoy_xml = buoy_xml
        self.x = ((buoy_xml.lon + 180) / 360 * map_object.width + map_object.offset) % buoy_xml.width
        self.y = ((buoy_xml.lat + 90) / 180 * map_object.height + map_object.offset) % buoy_xml.height
        self.ref = None
        self.card_ref = None

    def render(self):
        pass

    def render_card(self):
        pass

    def is_in_point(self):
        pass


def main():
    r = requests.get("https://ndbc.noaa.gov/activestations.xml")
    soup = BeautifulSoup(r.text)
    buoy_soup = soup.find_all(type="buoy")
    buoy_list = list(map(lambda b: FilteredXML(b), buoy_soup))
