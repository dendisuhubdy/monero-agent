# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class NEMDecryptedMessage(p.MessageType):
    MESSAGE_WIRE_TYPE = 76
    FIELDS = {
        1: ('payload', p.BytesType, 0),
    }

    def __init__(
        self,
        payload: bytes = None,
    ) -> None:
        self.payload = payload
