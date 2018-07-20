# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p
from .HDNodeType import HDNodeType


class PublicKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 12
    FIELDS = {
        1: ('node', HDNodeType, 0),  # required
        2: ('xpub', p.UnicodeType, 0),
    }

    def __init__(
        self,
        node: HDNodeType = None,
        xpub: str = None,
    ) -> None:
        self.node = node
        self.xpub = xpub
