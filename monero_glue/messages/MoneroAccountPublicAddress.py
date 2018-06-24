# Automatically generated by pb2py
from .. import protobuf as p


class MoneroAccountPublicAddress(p.MessageType):
    FIELDS = {
        1: ('m_spend_public_key', p.BytesType, 0),
        2: ('m_view_public_key', p.BytesType, 0),
    }

    def __init__(
        self,
        m_spend_public_key: bytes = None,
        m_view_public_key: bytes = None
    ) -> None:
        self.m_spend_public_key = m_spend_public_key
        self.m_view_public_key = m_view_public_key