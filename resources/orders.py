from ..requests import GETPage, POST, GETDetail
from ..response import Response
from ..dataclasses.orders import OrderData
from . import Resource


class Orders(Resource):
    _resource_path = '/orders'

    def get(self) -> Response:
        return GETPage().execute(url=self.url, headers=self.headers)

    def get_detail(self, id) -> Response:
        return GETDetail().execute(base_url=self.url, id=id, headers=self.headers)

    def create(self, order_data: OrderData) -> Response:
        return POST().execute(url=self.url, data=order_data.as_dict, headers=self.headers)
