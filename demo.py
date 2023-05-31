# demo.py

# import packages
import browser_cookie3 as browsercookie
import apirate.src as src
import requests, json

# get rat cookie from firefox in this case
rat = requests.utils.dict_from_cookiejar(browsercookie.firefox()).get('rat')

session = requests.Session()

pirate = src.Pirate(rat)
print(pirate.get_profilev2("balance").get("gold"))
