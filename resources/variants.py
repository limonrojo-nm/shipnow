from ..requests import GETPage, GETDetail, POST
from ..response import Response
from ..dataclasses.variants import VariantData
from . import Resource


class Variants(Resource):
    _resource_path = '/variants'

    def get(self, page: int = None) -> Response:
        return GETPage().execute(url=self.url, page=page, headers=self.headers)

    def get_detail(self, id) -> Response:
        return GETDetail().execute(base_url=self.url, id=id, headers=self.headers)

    def create(self, variant_data: VariantData) -> Response:
        return POST().execute(url=self.url, data=variant_data.as_dict, headers=self.headers)
