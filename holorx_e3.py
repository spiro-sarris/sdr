#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Holorx E3
# Generated: Sun Feb 17 10:46:21 2019
##################################################


from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import SimpleXMLRPCServer
import threading
import time


class holorx_e3(gr.top_block):

    def __init__(self, freq_lo_offset=60e3, freq_rftune=70e6, gain_rxa=0, gain_rxb=0):
        gr.top_block.__init__(self, "Holorx E3")

        ##################################################
        # Parameters
        ##################################################
        self.freq_lo_offset = freq_lo_offset
        self.freq_rftune = freq_rftune
        self.gain_rxa = gain_rxa
        self.gain_rxb = gain_rxb

        ##################################################
        # Variables
        ##################################################
        self.sps_output = sps_output = 1000
        self.server_port = server_port = 30000
        self.server_address = server_address = "192.168.10.184"
        self.samp_rate = samp_rate = 20e3

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_1 = zeromq.push_sink(gr.sizeof_gr_complex, 1, 'tcp://*:9998', 100, False, -1)
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_gr_complex, 1, 'tcp://*:9999', 100, False, -1)
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer((str(server_address), int(server_port)), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(('', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0.set_clock_source('internal', 0)
        self.uhd_usrp_source_0.set_time_source('external', 0)
        self.uhd_usrp_source_0.set_subdev_spec('A:A A:B', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(freq_rftune,freq_lo_offset), 0)
        self.uhd_usrp_source_0.set_gain(gain_rxa, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(freq_rftune,freq_lo_offset), 1)
        self.uhd_usrp_source_0.set_gain(gain_rxb, 1)
        self.uhd_usrp_source_0.set_antenna('RX2', 1)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=int(samp_rate/sps_output),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=int(samp_rate/sps_output),
                taps=None,
                fractional_bw=None,
        )
        self.blocks_tag_debug_0_0 = blocks.tag_debug(gr.sizeof_gr_complex*1, 'usrp_rx_a', ""); self.blocks_tag_debug_0_0.set_display(True)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_gr_complex*1, 'usrp_rx_b', ""); self.blocks_tag_debug_0.set_display(True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.rational_resampler_xxx_0, 0), (self.zeromq_push_sink_1, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.zeromq_push_sink_0, 0))
        self.connect((self.uhd_usrp_source_0, 1), (self.blocks_tag_debug_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_tag_debug_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.uhd_usrp_source_0, 1), (self.rational_resampler_xxx_0_0, 0))

    def get_freq_lo_offset(self):
        return self.freq_lo_offset

    def set_freq_lo_offset(self, freq_lo_offset):
        self.freq_lo_offset = freq_lo_offset
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq_rftune,self.freq_lo_offset), 0)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq_rftune,self.freq_lo_offset), 1)

    def get_freq_rftune(self):
        return self.freq_rftune

    def set_freq_rftune(self, freq_rftune):
        self.freq_rftune = freq_rftune
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq_rftune,self.freq_lo_offset), 0)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq_rftune,self.freq_lo_offset), 1)

    def get_gain_rxa(self):
        return self.gain_rxa

    def set_gain_rxa(self, gain_rxa):
        self.gain_rxa = gain_rxa
        self.uhd_usrp_source_0.set_gain(self.gain_rxa, 0)


    def get_gain_rxb(self):
        return self.gain_rxb

    def set_gain_rxb(self, gain_rxb):
        self.gain_rxb = gain_rxb
        self.uhd_usrp_source_0.set_gain(self.gain_rxb, 1)


    def get_sps_output(self):
        return self.sps_output

    def set_sps_output(self, sps_output):
        self.sps_output = sps_output

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
        "", "--freq-lo-offset", dest="freq_lo_offset", type="eng_float", default=eng_notation.num_to_str(60e3),
        help="Set freq_lo_offset [default=%default]")
    parser.add_option(
        "", "--freq-rftune", dest="freq_rftune", type="eng_float", default=eng_notation.num_to_str(70e6),
        help="Set freq_rftune [default=%default]")
    parser.add_option(
        "", "--gain-rxa", dest="gain_rxa", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set gain_rxa [default=%default]")
    parser.add_option(
        "", "--gain-rxb", dest="gain_rxb", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set gain_rxb [default=%default]")
    return parser


def main(top_block_cls=holorx_e3, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(freq_lo_offset=options.freq_lo_offset, freq_rftune=options.freq_rftune, gain_rxa=options.gain_rxa, gain_rxb=options.gain_rxb)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
