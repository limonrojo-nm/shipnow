from ..requests import GET
from ..response import Response
from . import Resource


class Stores(Resource):
    _resource_path = '/stores'

    def get(self) -> Response:
        return GET().execute(self.url, headers=self.headers)
