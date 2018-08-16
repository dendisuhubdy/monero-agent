# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .TezosContractID import TezosContractID


class TezosOriginationOp(p.MessageType):
    FIELDS = {
        1: ('source', TezosContractID, 0),
        2: ('fee', p.UVarintType, 0),
        3: ('counter', p.UVarintType, 0),
        4: ('gas_limit', p.UVarintType, 0),
        5: ('storage_limit', p.UVarintType, 0),
        6: ('manager_pubkey', p.BytesType, 0),
        7: ('balance', p.UVarintType, 0),
        8: ('spendable', p.BoolType, 0),
        9: ('delegatable', p.BoolType, 0),
        10: ('delegate', p.BytesType, 0),
        11: ('script', p.BytesType, 0),
    }

    def __init__(
        self,
        source: TezosContractID = None,
        fee: int = None,
        counter: int = None,
        gas_limit: int = None,
        storage_limit: int = None,
        manager_pubkey: bytes = None,
        balance: int = None,
        spendable: bool = None,
        delegatable: bool = None,
        delegate: bytes = None,
        script: bytes = None,
    ) -> None:
        self.source = source
        self.fee = fee
        self.counter = counter
        self.gas_limit = gas_limit
        self.storage_limit = storage_limit
        self.manager_pubkey = manager_pubkey
        self.balance = balance
        self.spendable = spendable
        self.delegatable = delegatable
        self.delegate = delegate
        self.script = script
