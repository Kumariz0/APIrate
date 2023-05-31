# apirate/src/seaofthieves.py
from .. import session, APIKeyMissingError, InvalidEndpointError


class Pirate:

    def __init__(self, api_key,):
        if api_key is None:
            # TODO write docs for getting RAT cookie
            raise APIKeyMissingError(
                "RAT Cookie is required. See https://github.com/Kumariz0/APIrate/wiki for how to retrieve an authentication token from Sea of Thieves.")
        self.session = session
        self.api_key_cookie = {'rat': api_key}
        self.headers = {'Referer': 'https://www.seaofthieves.com/'}

    def get_profilev2(self, endpoint):
        ALLOWED_ENDPOINTS = [
            "reputation",
            "balance",
            "status",
            "captaincy",
            "adventures",
            "chest",
            "achievements",
            "overview"
        ]
        """Gets data from the sea of thieves api server about your own pirate.

        Args:
            endpoint (string): The endpoint, of where you want to get data from. Allowed endpoint are: """ + ', '.join(ALLOWED_ENDPOINTS) + """
            
        Raises:
            InvalidEndpointError: Invalid endpoint

        Returns:
            dict: A dict with the information gathered from the endpoint.
        """
        BASE_URL = "https://www.seaofthieves.com/api/profilev2"
        if endpoint not in ALLOWED_ENDPOINTS:
            raise InvalidEndpointError(
                "Invalid endpoint. Allowed endpoints are: " + ', '.join(ALLOWED_ENDPOINTS))

        url = f"{BASE_URL}/{endpoint}"
        response = session.get(url, headers=self.headers,
                               cookies=self.api_key_cookie,)
        return response.json()

    def get_user(self, endpoint):
        ALLOWED_ENDPOINTS = [
            "get-suggested-friend",
            "playing",
            "get-recent-friends",
        ]
        """Gets data from the sea of thieves api server about your friends.

        Args:
            endpoint (string): The endpoint, of where you want to get data from. Allowed endpoint are: """ + ', '.join(ALLOWED_ENDPOINTS) + """
        
        Raises:
            InvalidEndpointError: Invalid endpoint

        Returns:
            dict: A dict with the information gathered from the endpoint.
        """
        BASE_URL = "https://www.seaofthieves.com/api/user"
        if endpoint not in ALLOWED_ENDPOINTS:
            raise InvalidEndpointError(
                "Invalid endpoint. Allowed endpoints are: " + ', '.join(ALLOWED_ENDPOINTS))

        url = f"{BASE_URL}/{endpoint}"
        response = session.get(url, headers=self.headers,
                               cookies=self.api_key_cookie,)
        return response.json()
    
    def get_ledger(self, endpoint):
        """Gets data from the sea of thieves api server about the global ledger.

        Args:
            endpoint (string): the endpoint, of where you want to get data from. Allowed endpoint are: GoldHoarders, OrderOfSouls, AthenasFortune, MerchantAlliance, ReapersBones

        Raises:
            InvalidEndpointError: Invalid endpoint

        Returns:
            dict: A dict with the information gathered from the endpoint.
        """
        ALLOWED_ENDPOINTS = [
            "GoldHoarders",
            "OrderOfSouls",
            "AthenasFortune",
            "MerchantAlliance",
            "ReapersBones"
        ]
        
        BASE_URL = "https://www.seaofthieves.com/api/ledger/global/"
        if endpoint not in ALLOWED_ENDPOINTS:
            raise InvalidEndpointError(
                "Invalid endpoint. Allowed endpoints are: " + ', '.join(ALLOWED_ENDPOINTS))

        url = f"{BASE_URL}/{endpoint}"
        response = session.get(url, headers=self.headers,
                               cookies=self.api_key_cookie,)
        return response.json()
