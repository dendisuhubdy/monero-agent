# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class NEMDecryptMessage(p.MessageType):
    MESSAGE_WIRE_TYPE = 75
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('network', p.UVarintType, 0),
        3: ('public_key', p.BytesType, 0),
        4: ('payload', p.BytesType, 0),
    }

    def __init__(
        self,
        address_n: List[int] = None,
        network: int = None,
        public_key: bytes = None,
        payload: bytes = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.network = network
        self.public_key = public_key
        self.payload = payload
