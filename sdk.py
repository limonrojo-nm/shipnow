from .connection import ConnectionSetup
from .resources import Resource
from .resources.ping import Ping
from .resources.stores import Stores
from .resources.orders import Orders
from .resources.variants import Variants
from .resources.webhooks import Webhooks


def lazy(sdk_instance: "SDK", private_attr: str, resource_class: Resource) -> Resource:
    """
    Loads a resource helper lazily
    NOTE: *Has side-effects!*: Assigns `private_attr` to `sdk_instance` with an instanced `resource_class`
    """
    if not hasattr(sdk_instance, private_attr):
        setattr(sdk_instance, private_attr, resource_class(connection_setup=sdk_instance.connection_setup))
    return getattr(sdk_instance, private_attr)


class SDK:
    def __init__(self, token):
        self._token = token

    @property
    def connection_setup(self): return ConnectionSetup(self._token)

    # Resources
    @property
    def ping(self) -> Ping: return lazy(self, "_ping", Ping)
    @property
    def stores(self) -> Stores: return lazy(self, "_stores", Stores)
    @property
    def orders(self) -> Orders: return lazy(self, "_orders", Orders)
    @property
    def variants(self) -> Variants: return lazy(self, "_variants", Variants)
    @property
    def webhooks(self) -> Webhooks: return lazy(self, "_webhooks", Webhooks)
