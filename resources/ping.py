from ..response import Response
from . import Resource
from ..requests import GET


class Ping(Resource):
    _resource_path = '/ping'

    def get(self) -> Response:
        return GET().execute(self.url, headers=self.headers)
