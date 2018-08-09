# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .CardanoTxInputType import CardanoTxInputType
from .CardanoTxOutputType import CardanoTxOutputType

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class CardanoSignTransaction(p.MessageType):
    MESSAGE_WIRE_TYPE = 303
    FIELDS = {
        1: ('inputs', CardanoTxInputType, p.FLAG_REPEATED),
        2: ('outputs', CardanoTxOutputType, p.FLAG_REPEATED),
        3: ('transactions_count', p.UVarintType, 0),
    }

    def __init__(
        self,
        inputs: List[CardanoTxInputType] = None,
        outputs: List[CardanoTxOutputType] = None,
        transactions_count: int = None,
    ) -> None:
        self.inputs = inputs if inputs is not None else []
        self.outputs = outputs if outputs is not None else []
        self.transactions_count = transactions_count
