# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class MoneroMultisigKLRki(p.MessageType):
    FIELDS = {
        1: ('K', p.BytesType, 0),
        2: ('L', p.BytesType, 0),
        3: ('R', p.BytesType, 0),
        4: ('ki', p.BytesType, 0),
    }

    def __init__(
        self,
        K: bytes = None,
        L: bytes = None,
        R: bytes = None,
        ki: bytes = None,
    ) -> None:
        self.K = K
        self.L = L
        self.R = R
        self.ki = ki