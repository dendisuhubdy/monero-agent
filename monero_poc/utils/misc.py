#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Dusan Klinec, ph4r05, 2018

import asyncio
import binascii
import collections
import json
import logging
import os
import random
import re
import signal
import string
import subprocess
import sys
import threading
import time
import traceback
from shlex import quote

import shellescape
from sarge import Capture, Feeder, run

from monero_glue.xmr import crypto

logger = logging.getLogger(__name__)


class CliPrompt(object):
    """
    Synchronous CLI confirmation waiter.
    """

    def __init__(self, pre_wait_hook=None, *args, **kwargs):
        self.in_confirmation = False
        self.conf_evt = None
        self.confirmed_result = False
        self.pre_wait_hook = pre_wait_hook

    def confirmation(self, confirmed):
        self.confirmed_result = confirmed
        self.in_confirmation = False
        self.conf_evt.set()

    def _init_wait(self):
        self.in_confirmation = True
        self.confirmed_result = False
        self.conf_evt = threading.Event()

    def wait_confirmation(self):
        """
        Synchronous waiting
        :return:
        """
        self._init_wait()
        if self.pre_wait_hook:
            self.pre_wait_hook()

        try:
            self.conf_evt.wait()
            return self.confirmed_result

        finally:
            self.in_confirmation = False

    async def async_wait_confirmation(self):
        """
        Asynchronous waiting
        Asyncio waiting not implemented.

        :return:
        """
        self._init_wait()
        try:
            # TODO: asyncio wait
            # TODO: eventlet could require another locking mechanism
            self.conf_evt.wait()
            return self.confirmed_result

        finally:
            self.in_confirmation = False

    def __enter__(self):
        self._init_wait()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.in_confirmation = False


def py_raw_input(question=None):
    """
    Python compatibility wrapper for standard raw_input()
    :param question:
    :return:
    """
    return input(question)


def gen_simple_passwd(n):
    """
    Generates simple alphanum passwd.
    TODO: stronger passwd
    :param n:
    :return:
    """
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(n)
    )


def parse_transfer_cmd(parts):
    """
    Parses transfer command format
    :param parts:
    :return:
    """

    priority = None
    mixin = None
    address = None
    amount = None
    payment_id = None

    ln_parts = len(parts)
    if ln_parts < 2:
        raise ValueError("Invalid format")

    addr_idx = 0
    p1_num = re.match(r"^[0-9]+$", parts[0])
    p2_num = re.match(r"^[0-9]+$", parts[1])
    if p1_num and p2_num:
        addr_idx = 2
        priority = int(parts[0])
        mixin = int(parts[1])

    elif p1_num and not p2_num:
        addr_idx = 1
        mixin = int(parts[0])

    else:
        addr_idx = 0

    if ln_parts == 2:
        address = parts[0]
        amount = float(parts[1])

    address = parts[addr_idx]
    amount = float(parts[addr_idx + 1])

    if ln_parts == addr_idx + 3:
        payment_id = parts[addr_idx + 2]

    return priority, mixin, address, amount, payment_id


class SargeLogFilter(logging.Filter):
    """Filters out debugging logs generated by sarge - output capture. It is way too verbose for debug"""

    def __init__(self, name="", *args, **kwargs):
        self.namex = name
        logging.Filter.__init__(self, *args, **kwargs)

    def filter(self, record):
        if record.levelno != logging.DEBUG:
            return 1

        try:
            # Parse messages are too verbose, skip.
            if record.name == "sarge.parse":
                return 0

            # Disable output processing message - length of one character.
            msg = record.getMessage()
            if "queued chunk of length 1" in msg:
                return 0

            return 1

        except Exception as e:
            logger.error("Exception in log filtering: %s" % e)

        return 1


def install_sarge_filter():
    """
    Installs Sarge log filter to avoid long 1char debug dumps
    :return:
    """
    for handler in logging.getLogger().handlers:
        handler.addFilter(SargeLogFilter("hnd"))
    logging.getLogger().addFilter(SargeLogFilter("root"))


def sarge_sigint(proc):
    """
    Sends sigint to sarge process
    :return:
    """
    proc.process_ready.wait()
    p = proc.process
    if not p:  # pragma: no cover
        raise ValueError("There is no subprocess")
    p.send_signal(signal.SIGINT)


def escape_shell(inp):
    """
    Shell-escapes input param
    :param inp:
    :return:
    """
    try:
        inp = inp.decode('utf8')
    except:
        pass

    try:
        return shellescape.quote(inp)
    except:
        pass

    quote(inp)


def add_readlines(lns, buff):
    """
    Cmd output processing helper
    :param lns:
    :param buff:
    :return:
    """
    if lns is None or len(lns) == 0:
        return buff
    buff += [x.decode("utf8") for x in lns]
    return buff


def wallet_enc_key(salt, password):
    """
    Chacha20 password derivation for view key storage
    :param salt:
    :param password:
    :return:
    """
    return crypto.pbkdf2(password, salt, count=2048)
