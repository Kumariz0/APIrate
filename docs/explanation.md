# Explanation

## What is this?

APIrate is a API wrapper for the API calls the Sea of Thieves website uses to get their data. It uses the so called RAT cookie to authenticate the user while getting the data. The RAT cookie is the authentication token that gets saved when logging in using a Microsoft account.

## How does it work?

You create a new Pirate object while passing in the RAT cookie. You can then call the functions on the Pirate object to get the data you want. The functions are named after the endpoints the Sea of Thieves website uses to get their data. For example the `get_profilev2()` function is named after the `/api/profilev2` endpoint. The `get_profilev2()` function returns a dictionary with the data from the endpoint. You can then call the `get()` function on the dictionary to get the data you want. For example the `get()` function can be used to get the gold of the player.

## How do I get the RAT cookie?

You can either login using your browser and the grab the cookie from the browser. Look in the [tutorials](./tutorials.md) for more information on how to do this.
!!! Tip
    It might be possible to get tha RAT cookie by letting the user login on you webstite like [merfolkslullaby](https://merfolkslullaby.com/) does. This is not tested yet.

