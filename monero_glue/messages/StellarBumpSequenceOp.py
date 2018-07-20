# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class StellarBumpSequenceOp(p.MessageType):
    MESSAGE_WIRE_TYPE = 221
    FIELDS = {
        1: ('source_account', p.UnicodeType, 0),
        2: ('bump_to', p.UVarintType, 0),
    }

    def __init__(
        self,
        source_account: str = None,
        bump_to: int = None,
    ) -> None:
        self.source_account = source_account
        self.bump_to = bump_to