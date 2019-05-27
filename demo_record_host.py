#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: SDR RX Test
# Author: Spiro Sarris
# Description: Phase and Path Length Difference of Two Receiver Channels
# Generated: Wed May 22 21:11:47 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import ettus
import numpy as np
import sip
import sys
import xmlrpclib
from gnuradio import qtgui


class demo_record_host(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "SDR RX Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("SDR RX Test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "demo_record_host")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.velocity_factor = velocity_factor = 0.69
        self.vec_length = vec_length = 1
        self.speed_of_light = speed_of_light = 299792458
        self.samp_rate = samp_rate = 1e6
        self.rx_gain_A2 = rx_gain_A2 = 60
        self.rf_freq = rf_freq = 432e6
        self.fft_size = fft_size = 1024
        self.client_address = client_address = "192.168.10.184"

        ##################################################
        # Blocks
        ##################################################
        self.tabs = Qt.QTabWidget()
        self.tabs_widget_0 = Qt.QWidget()
        self.tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_0)
        self.tabs_grid_layout_0 = Qt.QGridLayout()
        self.tabs_layout_0.addLayout(self.tabs_grid_layout_0)
        self.tabs.addTab(self.tabs_widget_0, 'Real-Time Display')
        self.top_grid_layout.addWidget(self.tabs, 0, 0, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rf_freq_range = Range(100e6, 6000e6, 1e6, 432e6, 100)
        self._rf_freq_win = RangeWidget(self._rf_freq_range, self.set_rf_freq, 'RF Freq', "counter_slider", float)
        self.tabs_grid_layout_0.addWidget(self._rf_freq_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.zeromq_pull_source_1_0_0 = zeromq.pull_source(gr.sizeof_char, 1024, 'tcp://192.168.10.184:4001', 100, True, -1)
        self.zeromq_pull_source_1_0 = zeromq.pull_source(gr.sizeof_char, 1024, 'tcp://192.168.10.184:4000', 100, True, -1)
        self.zeromq_pull_source_1 = zeromq.pull_source(gr.sizeof_gr_complex, vec_length, 'tcp://192.168.10.184:9998', 100, False, -1)
        self.xmlrpc_client0_0 = xmlrpclib.Server('http://192.168.10.184:30000')
        self.xmlrpc_client0 = xmlrpclib.Server('http://192.168.10.184:30000')
        self._rx_gain_A2_range = Range(0, 80, 1, 60, 100)
        self._rx_gain_A2_win = RangeWidget(self._rx_gain_A2_range, self.set_rx_gain_A2, 'RX Gain', "counter_slider", float)
        self.tabs_grid_layout_0.addWidget(self._rx_gain_A2_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	fft_size, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rf_freq, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [3, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-100, -40)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	fft_size, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-0.05, 0.05)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	fft_size, #size
        	firdes.WIN_HANN, #wintype
        	rf_freq, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.1)
        self.qtgui_freq_sink_x_0.set_y_axis(-100, -20)
        self.qtgui_freq_sink_x_0.set_y_label('Amplitude', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', 'RXA', 'RXB', '', '',
                  '', '', '', '', '']
        widths = [1, 2, 2, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	fft_size, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-0.05, 0.05)
        self.qtgui_const_sink_x_0.set_x_axis(-0.05, 0.05)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(True)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_const_sink_x_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*vec_length, samp_rate,True)
        self.blocks_null_sink_1_0 = blocks.null_sink(gr.sizeof_char*1024)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_char*1024)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*vec_length)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.zeromq_pull_source_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.zeromq_pull_source_1, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.zeromq_pull_source_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.zeromq_pull_source_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.zeromq_pull_source_1, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.zeromq_pull_source_1_0, 0), (self.blocks_null_sink_1, 0))
        self.connect((self.zeromq_pull_source_1_0_0, 0), (self.blocks_null_sink_1_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "demo_record_host")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_velocity_factor(self):
        return self.velocity_factor

    def set_velocity_factor(self, velocity_factor):
        self.velocity_factor = velocity_factor

    def get_vec_length(self):
        return self.vec_length

    def set_vec_length(self, vec_length):
        self.vec_length = vec_length

    def get_speed_of_light(self):
        return self.speed_of_light

    def set_speed_of_light(self, speed_of_light):
        self.speed_of_light = speed_of_light

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rf_freq, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rf_freq, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rx_gain_A2(self):
        return self.rx_gain_A2

    def set_rx_gain_A2(self, rx_gain_A2):
        self.rx_gain_A2 = rx_gain_A2
        self.xmlrpc_client0.set_rx_gain_A2(self.rx_gain_A2)

    def get_rf_freq(self):
        return self.rf_freq

    def set_rf_freq(self, rf_freq):
        self.rf_freq = rf_freq
        self.xmlrpc_client0_0.set_rf_freq(self.rf_freq)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rf_freq, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rf_freq, self.samp_rate)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_client_address(self):
        return self.client_address

    def set_client_address(self, client_address):
        self.client_address = client_address


def main(top_block_cls=demo_record_host, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
