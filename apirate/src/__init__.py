# apirate/src/__init__.py
import requests


class APIKeyMissingError(Exception):
    pass


class InvalidEndpointError(Exception):
    pass


session = requests.Session()

from .seaofthieves import Pirate