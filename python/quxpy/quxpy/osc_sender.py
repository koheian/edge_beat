# coding=utf-8
#
# python-osc ( https://pypi.org/project/python-osc/ ) is required.
#

from pythonosc import osc_message_builder, udp_client
from .list_util import flatten

class OscSender:
    def __init__(self, host, port):
        self.client = udp_client.SimpleUDPClient(host, port)

    def send(self, address, *args):
        msg = osc_message_builder.OscMessageBuilder(address=address)

        args = flatten(args)

        for arg in args:
            msg.add_arg(arg)

        msg = msg.build()

        self.client.send(msg)


osc_sender = None

def setup(host, port):
    global osc_sender
    osc_sender = OscSender(host, port)

def send(address, *args):
    global osc_sender
    osc_sender.send(address, args)