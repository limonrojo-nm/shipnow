from abc import ABC
import requests

from ..response import Response
from ..connection import ConnectionSetup
from ..constants import API_BASE_PATH


class Resource(ABC):
    _resource_path: str

    def __init__(self, connection_setup: ConnectionSetup):
        self._connection_setup = connection_setup

    @property
    def url(self): return f"{API_BASE_PATH}{self._resource_path}"
    @property
    def headers(self) -> dict: return self._connection_setup.headers

    # Actions -----------------------------------------------------------------
    # def _get(self, page=None) -> Response:
    #     params = dict()

    #     if page is not None:
    #         params["page"] = page

    #     return Response(requests.get(self.url, headers=self._connection_setup.headers, params=params))

    # def _post(self, data: dict) -> Response:
    #     return Response(requests.post(self.url, data=data, headers=self._connection_setup.headers))
