# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class MoneroWatchKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 533
    FIELDS = {
        1: ('watch_key', p.BytesType, 0),
        2: ('address', p.BytesType, 0),
    }

    def __init__(
        self,
        watch_key: bytes = None,
        address: bytes = None,
    ) -> None:
        self.watch_key = watch_key
        self.address = address
