from abc import ABC

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
