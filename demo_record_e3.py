#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: demo_record_e3
# Generated: Thu Feb 28 11:21:23 2019
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import SimpleXMLRPCServer
import ettus
import threading
import time


class demo_record_e3(gr.top_block):

    def __init__(self, freq=871.3e6, rx_gain=40):
        gr.top_block.__init__(self, "demo_record_e3")

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq
        self.rx_gain = rx_gain

        ##################################################
        # Variables
        ##################################################
        self.tuning_lo_offset = tuning_lo_offset = 60e3
        self.server_port = server_port = 30000
        self.server_address = server_address = "192.168.10.184"
        self.samp_rate = samp_rate = 1e6

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_1 = zeromq.push_sink(gr.sizeof_gr_complex, 1, 'tcp://*:9998', 100, False, -1)
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer((str(server_address), int(server_port)), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(('', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec('A:A A:B', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(freq,tuning_lo_offset), 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.zeromq_push_sink_1, 0))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq,self.tuning_lo_offset), 0)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq,self.tuning_lo_offset), 1)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)

        self.uhd_usrp_source_0.set_gain(self.rx_gain, 1)


    def get_tuning_lo_offset(self):
        return self.tuning_lo_offset

    def set_tuning_lo_offset(self, tuning_lo_offset):
        self.tuning_lo_offset = tuning_lo_offset
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq,self.tuning_lo_offset), 0)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq,self.tuning_lo_offset), 1)

    def get_server_port(self):
        return self.server_port

    def set_server_port(self, server_port):
        self.server_port = server_port

    def get_server_address(self):
        return self.server_address

    def set_server_address(self, server_address):
        self.server_address = server_address

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(871.3e6),
        help="Set freq [default=%default]")
    parser.add_option(
        "", "--rx-gain", dest="rx_gain", type="eng_float", default=eng_notation.num_to_str(40),
        help="Set rx_gain [default=%default]")
    return parser


def main(top_block_cls=demo_record_e3, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(freq=options.freq, rx_gain=options.rx_gain)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
