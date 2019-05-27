#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: rfnoc_rx_e3
# Generated: Wed May 22 20:14:11 2019
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


class rfnoc_rx_e3(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "rfnoc_rx_e3")

        ##################################################
        # Variables
        ##################################################
        self.vec_length = vec_length = 1
        self.device3 = variable_uhd_device3_0 = ettus.device3(uhd.device_addr_t( ",".join(('type=e3x0', "")) ))
        self.server_port = server_port = 30000
        self.server_address = server_address = "192.168.10.184"
        self.samp_rate = samp_rate = 1e6
        self.rx_gain_A2 = rx_gain_A2 = 60
        self.rf_freq = rf_freq = 871e6
        self.decim_rate = decim_rate = 500e3

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_1 = zeromq.push_sink(gr.sizeof_gr_complex, vec_length, 'tcp://*:9998', 100, False, -1)
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer((str(server_address), int(server_port)), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.uhd_rfnoc_streamer_radio_0 = ettus.rfnoc_radio(
            self.device3,
            uhd.stream_args( # Tx Stream Args
                cpu_format="fc32",
                otw_format="sc16",
                args="", # empty
            ),
            uhd.stream_args( # Rx Stream Args
                cpu_format="fc32",
                otw_format="sc16",
          args='',
            ),
            0, -1
        )
        self.uhd_rfnoc_streamer_radio_0.set_rate(samp_rate)

        self.uhd_rfnoc_streamer_radio_0.set_rx_freq(rf_freq, 0)
        self.uhd_rfnoc_streamer_radio_0.set_rx_gain(rx_gain_A2, 0)
        self.uhd_rfnoc_streamer_radio_0.set_rx_dc_offset(True, 0)


        self.uhd_rfnoc_streamer_radio_0.set_rx_bandwidth(samp_rate, 0)

        if "RX2":
            self.uhd_rfnoc_streamer_radio_0.set_rx_antenna("RX2", 0)


        self.uhd_rfnoc_streamer_radio_0.set_clock_source("internal")
        self.uhd_rfnoc_streamer_ddc_0 = ettus.rfnoc_generic(
            self.device3,
            uhd.stream_args( # TX Stream Args
                cpu_format="fc32", # TODO: This must be made an option
                otw_format="sc16",
                channels=range(1),
                args="input_rate={},output_rate={},fullscale={},freq={},gr_vlen={},{}".format(samp_rate, samp_rate, 1.0, 0, vec_length, "" if vec_length == 1 else "spp={}".format(vec_length)),
            ),
            uhd.stream_args( # RX Stream Args
                cpu_format="fc32", # TODO: This must be made an option
                otw_format="sc16",
                channels=range(1),
                args="gr_vlen={},{}".format(vec_length, "" if vec_length == 1 else "spp={}".format(vec_length)),
            ),
            "DDC", -1, -1,
        )
        for chan in xrange(1):
            self.uhd_rfnoc_streamer_ddc_0.set_arg("input_rate", float(samp_rate), chan)
            self.uhd_rfnoc_streamer_ddc_0.set_arg("output_rate", float(samp_rate), chan)
            self.uhd_rfnoc_streamer_ddc_0.set_arg("fullscale", 1.0, chan)
            self.uhd_rfnoc_streamer_ddc_0.set_arg("freq", 0, chan)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_rfnoc_streamer_ddc_0, 0), (self.zeromq_push_sink_1, 0))
        self.device3.connect(self.uhd_rfnoc_streamer_radio_0.get_block_id(), 0, self.uhd_rfnoc_streamer_ddc_0.get_block_id(), 0)

    def get_vec_length(self):
        return self.vec_length

    def set_vec_length(self, vec_length):
        self.vec_length = vec_length

    def get_variable_uhd_device3_0(self):
        return self.variable_uhd_device3_0

    def set_variable_uhd_device3_0(self, variable_uhd_device3_0):
        self.variable_uhd_device3_0 = variable_uhd_device3_0

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
        self.uhd_rfnoc_streamer_radio_0.set_rate(self.samp_rate)
        for i in xrange(1):
            self.uhd_rfnoc_streamer_ddc_0.set_arg("input_rate", float(self.samp_rate), i)
        for i in xrange(1):
            self.uhd_rfnoc_streamer_ddc_0.set_arg("output_rate", float(self.samp_rate), i)

    def get_rx_gain_A2(self):
        return self.rx_gain_A2

    def set_rx_gain_A2(self, rx_gain_A2):
        self.rx_gain_A2 = rx_gain_A2

        self.uhd_rfnoc_streamer_radio_0.set_rx_gain(self.rx_gain_A2, 0)

    def get_rf_freq(self):
        return self.rf_freq

    def set_rf_freq(self, rf_freq):
        self.rf_freq = rf_freq

        self.uhd_rfnoc_streamer_radio_0.set_rx_freq(self.rf_freq, 0)

    def get_decim_rate(self):
        return self.decim_rate

    def set_decim_rate(self, decim_rate):
        self.decim_rate = decim_rate


def main(top_block_cls=rfnoc_rx_e3, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
