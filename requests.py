from copy import copy
from abc import ABC, abstractmethod
import requests

from .response import Response


# -----------------------------------------------------------------------------
# Base Requests

class HTTPRequest(ABC):
    _core = requests
    @abstractmethod
    def execute(self, *args, **kwargs) -> Response: pass

    @property
    def core(self): return self._core


class GET(HTTPRequest):
    def execute(self, url: str, params: dict = {}, headers: dict = {}) -> Response:
        return Response(self.core.get(url=url, params=params, headers=headers))


class POST(HTTPRequest):
    def execute(self, url: str, data: dict = {}, headers: dict = {}) -> Response:
        return Response(self.core.post(url=url, json=data, headers=headers))


class PUT(HTTPRequest):
    def execute(self, url: str, data: dict = {}, headers: dict = {}) -> Response:
        return Response(self.core.put(url=url, data=data, headers=headers))


class PATCH(HTTPRequest):
    def execute(self, url: str, data: dict = {}, headers: dict = {}) -> Response:
        return Response(self.core.patch(url=url, data=data, headers=headers))


class DELETE(HTTPRequest):
    def execute(self, url: str, data: dict = {}, headers: dict = {}) -> Response:
        return Response(self.core.delete(url=url, data=data, headers=headers))


# -----------------------------------------------------------------------------
# Advanced Requests

class GETPage(HTTPRequest):
    def execute(self, url: str, page: int, params: dict = {}, headers: dict = {}) -> Response:
        merged_params = copy(params)
        merged_params["page"] = page
        return Response(self.core.get(url=url, params=merged_params, headers=headers))


class GETDetail(HTTPRequest):
    def execute(self, base_url: str, id, params: dict = {}, headers: dict = {}) -> Response:
        """
        Perfeforms a GET against `base_url`, appending `id`"

        Args:
            base_url (str): NOTE: `base_url` must not contain trailing slash. Example: https://api.shipnow.com.ar/orders
            id: id of the resource
            params (dict, optional): query params to be appended to the request. Defaults to {}.
            headers (dict, optional): request headers . Defaults to {}.

        Returns:
            Response
        """
        url = f"{base_url}/{id}"
        return Response(self.core.get(url=url, params=params, headers=headers))


class DELETEIdentifier(HTTPRequest):
    def execute(self, base_url: str, id: str, headers: dict = {}) -> Response:
        """
        Perfeforms a DELETE against `base_url`, appending `id`"

        Args:
            base_url (str): NOTE: `base_url` must not contain trailing slash. Example: https://api.shipnow.com.ar/orders
            id (int): id of the resource
            params (dict, optional): query params to be appended to the request. Defaults to {}.
            headers (dict, optional): request headers . Defaults to {}.

        Returns:
            Response
        """
        url = f"{base_url}/{id}"
        return Response(self.core.delete(url=url, headers=headers))
