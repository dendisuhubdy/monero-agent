#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Dusan Klinec, ph4r05, 2018

import os
import unittest
import pkg_resources
import aiounittest
import binascii

from monero_serialize import xmrserialize, xmrtypes
from monero_glue import trezor, trezor_lite, monero, common, crypto, agent_lite
import zlib


class AgentLiteTest(aiounittest.AsyncTestCase):
    """Simple tests"""

    def __init__(self, *args, **kwargs):
        super(AgentLiteTest, self).__init__(*args, **kwargs)

    async def test_tx_sign_simple(self):
        """
        Testing tx signature, simple, multiple inputs
        :return:
        """
        unsigned_tx_c = pkg_resources.resource_string(__name__, os.path.join('data', 'tsx_uns01.txt'))
        unsigned_tx = zlib.decompress(binascii.unhexlify(unsigned_tx_c))

        await self.tx_sign(unsigned_tx)

    async def test_tx_sign(self):
        """
        Testing tx signature, one input. non-simple RCT
        :return:
        """
        unsigned_tx_c = pkg_resources.resource_string(__name__, os.path.join('data', 'tsx_uns02.txt'))
        unsigned_tx = zlib.decompress(binascii.unhexlify(unsigned_tx_c))
        await self.tx_sign(unsigned_tx)

    async def test_tx_sign_sub_dest(self):
        """
        Testing tx signature, one input. non-simple RCT
        :return:
        """
        unsigned_tx_c = pkg_resources.resource_string(__name__, os.path.join('data', 'tsx_uns03.txt'))
        unsigned_tx = zlib.decompress(binascii.unhexlify(unsigned_tx_c))
        await self.tx_sign(unsigned_tx)

    async def test_tx_sign_sub_2dest(self):
        """
        Testing tx signature, one input. non-simple RCT
        :return:
        """
        unsigned_tx_c = pkg_resources.resource_string(__name__, os.path.join('data', 'tsx_uns04.txt'))
        unsigned_tx = zlib.decompress(binascii.unhexlify(unsigned_tx_c))
        await self.tx_sign(unsigned_tx)

    async def tx_sign(self, unsigned_tx):
        """
        Tx sign test with given unsigned transaction data
        :param unsigned_tx:
        :return:
        """
        reader = xmrserialize.MemoryReaderWriter(bytearray(unsigned_tx))
        ar = xmrserialize.Archive(reader, False)
        unsig = xmrtypes.UnsignedTxSet()
        await ar.message(unsig)

        tagent = self.init_agent()
        txes = await tagent.transfer_unsigned(unsig)
        self.receive(txes[0])

    def receive(self, tx):
        """
        Test transaction receive with known view/spend keys of destinations.
        :return:
        """
        wallet_creds = [self.get_creds(), self.get_creds_01(), self.get_creds_02()]
        wallet_subs = [None] * len(wallet_creds)

        # Precompute subaddresses.
        for idx, creds in enumerate(wallet_creds):
            wallet_subs[idx] = {}
            for account in range(0, 10):
                monero.compute_subaddresses(creds, account, range(200), wallet_subs[idx])

        pass

    def get_creds(self):
        """
        Wallet credentials
        :return:
        """
        return monero.AccountCreds.new_wallet(
            priv_view_key=crypto.b16_to_scalar(b'4ce88c168e0f5f8d6524f712d5f8d7d83233b1e7a2a60b5aba5206cc0ea2bc08'),
            priv_spend_key=crypto.b16_to_scalar(b'f2644a3dd97d43e87887e74d1691d52baa0614206ad1b0c239ff4aa3b501750a'))

    def get_creds_01(self):
        """
        Wallet 02 credentials
        :return:
        """
        return monero.AccountCreds.new_wallet(
            priv_view_key=crypto.b16_to_scalar(b'42ba20adb337e5eca797565be11c9adb0a8bef8c830bccc2df712535d3b8f608'),
            priv_spend_key=crypto.b16_to_scalar(b'b0ef6bd527b9b23b9ceef70dc8b4cd1ee83ca14541964e764ad23f5151204f0f'))

    def get_creds_02(self):
        """
        Wallet 01 credentials
        :return:
        """
        return monero.AccountCreds.new_wallet(
            priv_view_key=crypto.b16_to_scalar(b'9e7aba8ae9ee134e5d5464d9145a4db26793d7411af7d06f20e755cb2a5ad50f'),
            priv_spend_key=crypto.b16_to_scalar(b'283d8bab1aeaee8f8b5aed982fc894c67d3e03db9006e488321c053f5183310d'))

    def init_trezor(self):
        """
        Initialize new trezor instance
        :return:
        """
        trez = trezor_lite.TrezorLite()
        trez.creds = self.get_creds()
        return trez

    def init_agent(self):
        """
        Initialize new agent instance
        :return:
        """
        return agent_lite.Agent(self.init_trezor())


if __name__ == "__main__":
    unittest.main()  # pragma: no cover


