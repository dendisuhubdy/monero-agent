# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MoneroRingCtSig import MoneroRingCtSig
from .MoneroTransactionRsigData import MoneroTransactionRsigData


class MoneroTransactionAllOutSetAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 514
    FIELDS = {
        1: ('extra', p.BytesType, 0),
        2: ('tx_prefix_hash', p.BytesType, 0),
        3: ('rsig_data', MoneroTransactionRsigData, 0),
        4: ('rv', MoneroRingCtSig, 0),
    }

    def __init__(
        self,
        extra: bytes = None,
        tx_prefix_hash: bytes = None,
        rsig_data: MoneroTransactionRsigData = None,
        rv: MoneroRingCtSig = None,
    ) -> None:
        self.extra = extra
        self.tx_prefix_hash = tx_prefix_hash
        self.rsig_data = rsig_data
        self.rv = rv
