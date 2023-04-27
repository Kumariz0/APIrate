import os
import sys
import time
import random
import string
import json
import requests
import pathlib
import browser_cookie3
import http.cookiejar

browser = input("""Enter the browser you want to use:
    1: Chrome
    2: Firefox
""")

# define the cookie jar and fill it
tmp_cookies = browser_cookie3.firefox(domain_name='seaofthieves.com')

cookie_jar = http.cookiejar.MozillaCookieJar('cookies.txt')
for cookie in tmp_cookies:
    cookie_jar.set_cookie(cookie)
cookie_jar.save("./cookie/cookies.txt",ignore_discard=True, ignore_expires=True)


# Create a requests.Session object and assign the cookie jar to its cookies attribute
s = requests.Session()
s.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Accept-Language": "en-US,en"
}
s.cookies = cookie_jar

# Make the request
response = s.get("https://www.seaofthieves.com/api/profilev2/balance")
print(response.text)