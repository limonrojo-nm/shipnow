from ..response import Response
from . import Resource
from ..requests import GET, POST, DELETEIdentifier, GETDetail
from ..dataclasses.webhooks import WebhookData


class Webhooks(Resource):
    _resource_path = '/webhooks'

    def get(self) -> Response:
        return GET().execute(self.url, headers=self.headers)

    def get_detail(self, id) -> Response:
        return GETDetail().execute(base_url=self.url, id=id, headers=self.headers)

    def create(self, data: WebhookData) -> Response:
        return POST().execute(self.url, data=data.as_dict, headers=self.headers)

    def delete(self, id: str) -> Response:
        return DELETEIdentifier().execute(self.url, id=id, headers=self.headers)
