# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class WordRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 46
    FIELDS = {
        1: ('type', p.UVarintType, 0),
    }

    def __init__(
        self,
        type: int = None,
    ) -> None:
        self.type = type
