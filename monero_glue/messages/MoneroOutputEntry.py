# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MoneroRctKey import MoneroRctKey


class MoneroOutputEntry(p.MessageType):
    FIELDS = {
        1: ('idx', p.UVarintType, 0),
        2: ('key', MoneroRctKey, 0),
    }

    def __init__(
        self,
        idx: int = None,
        key: MoneroRctKey = None,
    ) -> None:
        self.idx = idx
        self.key = key
