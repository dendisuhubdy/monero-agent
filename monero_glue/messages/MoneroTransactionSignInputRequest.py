# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MoneroTransactionSourceEntry import MoneroTransactionSourceEntry


class MoneroTransactionSignInputRequest(p.MessageType):
    FIELDS = {
        1: ('src_entr', MoneroTransactionSourceEntry, 0),
        2: ('vini', p.BytesType, 0),
        3: ('vini_hmac', p.BytesType, 0),
        4: ('pseudo_out', p.BytesType, 0),
        5: ('pseudo_out_hmac', p.BytesType, 0),
        6: ('alpha_enc', p.BytesType, 0),
        7: ('spend_enc', p.BytesType, 0),
    }

    def __init__(
        self,
        src_entr: MoneroTransactionSourceEntry = None,
        vini: bytes = None,
        vini_hmac: bytes = None,
        pseudo_out: bytes = None,
        pseudo_out_hmac: bytes = None,
        alpha_enc: bytes = None,
        spend_enc: bytes = None,
    ) -> None:
        self.src_entr = src_entr
        self.vini = vini
        self.vini_hmac = vini_hmac
        self.pseudo_out = pseudo_out
        self.pseudo_out_hmac = pseudo_out_hmac
        self.alpha_enc = alpha_enc
        self.spend_enc = spend_enc
