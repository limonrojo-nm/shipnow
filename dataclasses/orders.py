from dataclasses import dataclass
from typing import List
from .common import WithAsDict


@dataclass
class ShipToData(WithAsDict):
    name: str
    last_name: str
    zip_code: int
    address_line: str
    city: str
    state: str
    email: str


@dataclass
class ItemData(WithAsDict):
    external_reference: str
    quantity: int


@dataclass
class OrderData(WithAsDict):
    external_reference: str
    ship_to: ShipToData
    items: List[ItemData]
    store_id: str
    status: str
