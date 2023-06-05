# Using APIrate

!!! info ""
    To use APIrate first of make shure you have it installed. When installeg you can import it.

## Demo

We are going to use the demo.py file for this example.

```python
# demo.py

import APIrate as APIrate
import browser_cookie3 as browsercookie
import requests

rat = requests.utils.dict_from_cookiejar(browsercookie.firefox()).get('rat')

pirate = APIrate.Pirate(rat)
print(pirate.get_profilev2("balance").get("gold"))
```

First of in line 3-5 we import the necessary modules. We are going to use the browser_cookie3 module to get the necessary `RAT` cookie the Sea of Thieves website uses to authenticate you. The requests module is helping with grabing the cookie from the browser.

```python
rat = requests.utils.dict_from_cookiejar(browsercookie.firefox()).get('rat')
```

This line is grabbing the cookie from the browser. You can use any browser you want. Just change the `browsercookie.firefox()` to the browser you want to use. For example `browsercookie.chrome()`.

```python
rat = requests.utils.dict_from_cookiejar(browsercookie.chrome()).get('rat')
```

You can break this line down to the following:

```python
cookie_jar = browsercookie.firefox()
cookie_dict = requests.utils.dict_from_cookiejar(cookie_jar)
rat = cookie_dict.get('rat')
```

- `browsercookie.firefox()` - This is a function that returns a `CookieJar` object containing cookies stored by Firefox.
- `requests.utils.dict_from_cookiejar()` - This is a function provided by the `requests` library that converts a `CookieJar` object into a dictionary.
- `.get('rat')` - This retrieves the value of the `'rat'` key from the dictionary returned by `dict_from_cookiejar()`.

In line 9 we define a Pirate object. This object is the player profile and contains the RAT cookie that you have to pass into it while defining it.

```python
pirate = APIrate.Pirate(rat)
```

Finaly we print the gold of the player. This is done by calling the `get_profilev2()` function and passing in the `balance` endpoint. This will return a dictionary with the balance of the player. The balance for example is made up of the players title, doubloons, gold, ancient coins and the profile image. We then get the gold by calling the `get()` function on the dictionary and passing in the `gold` key.

```python
print(pirate.get_profilev2("balance").get("gold"))
```
