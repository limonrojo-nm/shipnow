from .constants import TOKEN_PREFIX


class ConnectionSetup:
    def __init__(self, token: str):
        self._token = token

    @property
    def headers(self) -> dict: return {"Authorization": f"{TOKEN_PREFIX} {self._token}"}
