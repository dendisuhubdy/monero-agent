#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Dusan Klinec, ph4r05, 2018

from monero_glue.xmr import common, crypto


def compute_tx_key(spend_key_private, tx_prefix_hash, salt=None, rand_mult=None):
    """

    :param spend_key_private:
    :param tx_prefix_hash:
    :param salt:
    :param rand_mult:
    :return:
    """
    if not salt:
        salt = common.random_bytes(32)

    if not rand_mult:
        rand_mult_num = crypto.random_scalar()
        rand_mult = crypto.encodeint(rand_mult_num)
    else:
        rand_mult_num = crypto.decodeint(rand_mult)

    rand_inp = crypto.sc_add(spend_key_private, rand_mult_num)
    passwd = common.keccak_2hash(crypto.encodeint(rand_inp) + tx_prefix_hash)
    tx_key = common.pbkdf2(passwd, salt, count=100)
    return tx_key, salt, rand_mult





