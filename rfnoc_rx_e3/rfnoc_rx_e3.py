#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: rfnoc_rx_e3
# Generated: Sun Mar 24 20:07:07 2019
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import ettus


class rfnoc_rx_e3(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "rfnoc_rx_e3")

        ##################################################
        # Variables
        ##################################################
        self.device3 = variable_uhd_device3_0 = ettus.device3(uhd.device_addr_t( ",".join(('type=e3x0', "")) ))
        self.samp_rate = samp_rate = 1e6
        self.rx_gain_A2 = rx_gain_A2 = 30
        self.rx_gain_A1 = rx_gain_A1 = 60
        self.rf_freq = rf_freq = 432e6
        self.decim_rate = decim_rate = 500e3

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_push_sink_1 = zeromq.push_sink(gr.sizeof_gr_complex, 1, 'tcp://*:9998', 100, False, -1)
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
        self.uhd_rfnoc_streamer_radio_0.set_rx_gain(rx_gain_A1, 0)
        self.uhd_rfnoc_streamer_radio_0.set_rx_dc_offset(True, 0)


        self.uhd_rfnoc_streamer_radio_0.set_rx_bandwidth(samp_rate, 0)

        if "RX2":
            self.uhd_rfnoc_streamer_radio_0.set_rx_antenna("RX2", 0)


        self.uhd_rfnoc_streamer_radio_0.set_clock_source("internal")



        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_rfnoc_streamer_radio_0, 0), (self.zeromq_push_sink_1, 0))

    def get_variable_uhd_device3_0(self):
        return self.variable_uhd_device3_0

    def set_variable_uhd_device3_0(self, variable_uhd_device3_0):
        self.variable_uhd_device3_0 = variable_uhd_device3_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_rfnoc_streamer_radio_0.set_rate(self.samp_rate)

    def get_rx_gain_A2(self):
        return self.rx_gain_A2

    def set_rx_gain_A2(self, rx_gain_A2):
        self.rx_gain_A2 = rx_gain_A2

    def get_rx_gain_A1(self):
        return self.rx_gain_A1

    def set_rx_gain_A1(self, rx_gain_A1):
        self.rx_gain_A1 = rx_gain_A1

        self.uhd_rfnoc_streamer_radio_0.set_rx_gain(self.rx_gain_A1, 0)

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
