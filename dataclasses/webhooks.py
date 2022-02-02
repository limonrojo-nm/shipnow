from dataclasses import dataclass
from typing import List
from .common import WithAsDict


@dataclass
class WebhookFilterData(WithAsDict):
    topics: List[str]


@dataclass
class WebhookData(WithAsDict):
    url: str
    filters: WebhookFilterData
    active: bool
