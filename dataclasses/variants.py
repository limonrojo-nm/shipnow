from dataclasses import dataclass
from .common import WithAsDict


@dataclass
class VariantData(WithAsDict):
    external_reference: str
    title: str
