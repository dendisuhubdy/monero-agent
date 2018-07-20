# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class EthereumMessageSignature(p.MessageType):
    MESSAGE_WIRE_TYPE = 66
    FIELDS = {
        1: ('address', p.BytesType, 0),
        2: ('signature', p.BytesType, 0),
    }

    def __init__(
        self,
        address: bytes = None,
        signature: bytes = None,
    ) -> None:
        self.address = address
        self.signature = signature
