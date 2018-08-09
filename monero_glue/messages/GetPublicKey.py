# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class GetPublicKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 11
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('ecdsa_curve_name', p.UnicodeType, 0),
        3: ('show_display', p.BoolType, 0),
        4: ('coin_name', p.UnicodeType, 0),  # default=Bitcoin
        5: ('script_type', p.UVarintType, 0),  # default=SPENDADDRESS
    }

    def __init__(
        self,
        address_n: List[int] = None,
        ecdsa_curve_name: str = None,
        show_display: bool = None,
        coin_name: str = None,
        script_type: int = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.ecdsa_curve_name = ecdsa_curve_name
        self.show_display = show_display
        self.coin_name = coin_name
        self.script_type = script_type
