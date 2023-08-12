from fixtures.register.api import RegisterController
from fixtures.requests import Client


class ClientApp:
    def __init__(self, url):
        self.url = url
        self.client = Client
        self.register = RegisterController(self)
