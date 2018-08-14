# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MoneroTransactionDestinationEntry import MoneroTransactionDestinationEntry


class MoneroTransactionSetOutputRequest(p.MessageType):
    FIELDS = {
        1: ('dst_entr', MoneroTransactionDestinationEntry, 0),
        2: ('dst_entr_hmac', p.BytesType, 0),
    }

    def __init__(
        self,
        dst_entr: MoneroTransactionDestinationEntry = None,
        dst_entr_hmac: bytes = None,
    ) -> None:
        self.dst_entr = dst_entr
        self.dst_entr_hmac = dst_entr_hmac
