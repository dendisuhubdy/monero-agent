# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MoneroTransactionSourceEntry import MoneroTransactionSourceEntry


class MoneroTransactionSetInputRequest(p.MessageType):
    FIELDS = {
        1: ('version', p.UVarintType, 0),
        2: ('src_entr', p.BytesType, 0),
        3: ('src_entr_obj', MoneroTransactionSourceEntry, 0),
    }

    def __init__(
        self,
        version: int = None,
        src_entr: bytes = None,
        src_entr_obj: MoneroTransactionSourceEntry = None,
    ) -> None:
        self.version = version
        self.src_entr = src_entr
        self.src_entr_obj = src_entr_obj
