# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class ApplyFlags(p.MessageType):
    MESSAGE_WIRE_TYPE = 28
    FIELDS = {
        1: ('flags', p.UVarintType, 0),
    }

    def __init__(
        self,
        flags: int = None,
    ) -> None:
        self.flags = flags
