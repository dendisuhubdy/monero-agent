# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p
from .MoneroRingCtSig import MoneroRingCtSig


class MoneroTransactionAllOutSetAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 507
    FIELDS = {
        1: ('extra', p.BytesType, 0),
        2: ('tx_prefix_hash', p.BytesType, 0),
        3: ('rv', MoneroRingCtSig, 0),
    }

    def __init__(
        self,
        extra: bytes = None,
        tx_prefix_hash: bytes = None,
        rv: MoneroRingCtSig = None,
    ) -> None:
        self.extra = extra
        self.tx_prefix_hash = tx_prefix_hash
        self.rv = rv
