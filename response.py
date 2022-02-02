from math import ceil
import requests


class Response:
    def __init__(self, original_response: requests.Response):
        self._original_response = original_response

    @property
    def json(self) -> dict: return self._original_response.json()
    @property
    def text(self) -> str: return self._original_response.text
    @property
    def headers(self) -> dict: return self._original_response.headers

    @property
    def current_page(self) -> int: return int(self.headers['x-page'])
    @property
    def items_per_page(self) -> int: return int(self.headers['x-per-page'])
    @property
    def items_total(self) -> int: return int(self.headers['x-total'])
    @property
    def pages_total(self) -> int: return int(ceil(self.items_total / self.items_per_page))
    @property
    def is_last_page(self) -> bool: return self.pages_total == self.current_page
