#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Holo RX
# Author: Spiro Sarris
# Description: Phase and Path Length Difference of Two Receiver Channels
# Generated: Thu Aug 16 16:19:06 2018
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from fft_bin_select import fft_bin_select  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import zeromq
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from to_mag_db import to_mag_db  # grc-generated hier_block
import numpy as np
import sip
import xmlrpclib


class holorx_host(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Holo RX")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Holo RX")
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

        self.settings = Qt.QSettings("GNU Radio", "holorx_host")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.seconds_record = seconds_record = 60
        self.samp_rate = samp_rate = 200
        self.gui_update_sec = gui_update_sec = 1
        self.gain_rxb = gain_rxb = 0
        self.gain_rxa = gain_rxa = 0
        self.freq_rftune = freq_rftune = 69999953
        self.freq_lo_offset = freq_lo_offset = 60e3
        self.fft_size = fft_size = 128
        self.client_address = client_address = "192.168.10.184"

        ##################################################
        # Blocks
        ##################################################
        self.tabs = Qt.QTabWidget()
        self.tabs_widget_0 = Qt.QWidget()
        self.tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_0)
        self.tabs_grid_layout_0 = Qt.QGridLayout()
        self.tabs_layout_0.addLayout(self.tabs_grid_layout_0)
        self.tabs.addTab(self.tabs_widget_0, 'RX 2 Channels')
        self.top_grid_layout.addWidget(self.tabs, 0,0,1,1)
        self.zeromq_pull_source_1 = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://192.168.10.184:9998', 100, False, -1)
        self.zeromq_pull_source_0 = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://192.168.10.184:9999', 100, False, -1)
        self.xmlrpc_client1 = xmlrpclib.Server('http://192.168.10.184:30000')
        self.xmlrpc_client0_0_0 = xmlrpclib.Server('http://192.168.10.184:30000')
        self.xmlrpc_client0_0 = xmlrpclib.Server('http://192.168.10.184:30000')
        self.xmlrpc_client0 = xmlrpclib.Server('http://192.168.10.184:30000')
        self.to_mag_db_0_3 = to_mag_db()
        self.to_mag_db_0_1 = to_mag_db()
        self.to_mag_db_0_0 = to_mag_db()
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            2
        )
        self.qtgui_number_sink_0_0_0.set_update_time(gui_update_sec)
        self.qtgui_number_sink_0_0_0.set_title('Difference A-B')
        
        labels = ['Magnitude (dB)', 'Phase (deg)', 'A - B', '', '',
                  '', '', '', '', '']
        units = ['dB', 'degrees', 'dB', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(2):
            self.qtgui_number_sink_0_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_number_sink_0_0_0_win, 3,1,2,1)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            2
        )
        self.qtgui_number_sink_0_0.set_update_time(gui_update_sec)
        self.qtgui_number_sink_0_0.set_title('Magnitude (dB)')
        
        labels = ['RXA', 'RXB', 'RXB', '', '',
                  '', '', '', '', '']
        units = ['dB', 'dB', 'dB', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(2):
            self.qtgui_number_sink_0_0.set_min(i, -1)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_number_sink_0_0_win, 1,1,2,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	fft_size, #size
        	firdes.WIN_HANN, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(gui_update_sec)
        self.qtgui_freq_sink_x_0.set_y_axis(-160, -20)
        self.qtgui_freq_sink_x_0.set_y_label('FFT Amplitude', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['RXA', 'RXB', 'RXB', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 2, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
        self._gain_rxb_range = Range(0, 80, 1, 0, 1)
        self._gain_rxb_win = RangeWidget(self._gain_rxb_range, self.set_gain_rxb, 'Gain RXB', "counter", float)
        self.tabs_grid_layout_0.addWidget(self._gain_rxb_win, 2,0,1,1)
        self._gain_rxa_range = Range(0, 80, 1, 0, 1)
        self._gain_rxa_win = RangeWidget(self._gain_rxa_range, self.set_gain_rxa, 'Gain RXA', "counter", float)
        self.tabs_grid_layout_0.addWidget(self._gain_rxa_win, 1,0,1,1)
        self._freq_rftune_range = Range(10e6, 6e9, 1, 69999953, 1)
        self._freq_rftune_win = RangeWidget(self._freq_rftune_range, self.set_freq_rftune, 'Freq RF Tune', "counter", float)
        self.tabs_grid_layout_0.addWidget(self._freq_rftune_win, 3,0,1,1)
        self._freq_lo_offset_range = Range(0, 1e6, 1, 60e3, 1)
        self._freq_lo_offset_win = RangeWidget(self._freq_lo_offset_range, self.set_freq_lo_offset, 'Freq LO Offset', "counter", float)
        self.tabs_grid_layout_0.addWidget(self._freq_lo_offset_win, 4,0,1,1)
        self.fft_bin_select_B = fft_bin_select(
            fft_size=fft_size,
            nskip=1,
        )
        self.fft_bin_select_A = fft_bin_select(
            fft_size=fft_size,
            nskip=1,
        )
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((180/np.pi, ))
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, seconds_record*int(samp_rate/fft_size))
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, 'test500MHz_fft128.iq', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_divide_xx_0 = blocks.divide_cc(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_complex_to_arg_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_head_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.to_mag_db_0_3, 0))    
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_number_sink_0_0_0, 1))    
        self.connect((self.fft_bin_select_A, 0), (self.blocks_divide_xx_0, 0))    
        self.connect((self.fft_bin_select_A, 0), (self.to_mag_db_0_0, 0))    
        self.connect((self.fft_bin_select_B, 0), (self.blocks_divide_xx_0, 1))    
        self.connect((self.fft_bin_select_B, 0), (self.to_mag_db_0_1, 0))    
        self.connect((self.to_mag_db_0_0, 0), (self.qtgui_number_sink_0_0, 0))    
        self.connect((self.to_mag_db_0_1, 0), (self.qtgui_number_sink_0_0, 1))    
        self.connect((self.to_mag_db_0_3, 0), (self.qtgui_number_sink_0_0_0, 0))    
        self.connect((self.zeromq_pull_source_0, 0), (self.fft_bin_select_B, 0))    
        self.connect((self.zeromq_pull_source_0, 0), (self.qtgui_freq_sink_x_0, 1))    
        self.connect((self.zeromq_pull_source_1, 0), (self.fft_bin_select_A, 0))    
        self.connect((self.zeromq_pull_source_1, 0), (self.qtgui_freq_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "holorx_host")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_seconds_record(self):
        return self.seconds_record

    def set_seconds_record(self, seconds_record):
        self.seconds_record = seconds_record
        self.blocks_head_0.set_length(self.seconds_record*int(self.samp_rate/self.fft_size))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_head_0.set_length(self.seconds_record*int(self.samp_rate/self.fft_size))

    def get_gui_update_sec(self):
        return self.gui_update_sec

    def set_gui_update_sec(self, gui_update_sec):
        self.gui_update_sec = gui_update_sec
        self.qtgui_number_sink_0_0_0.set_update_time(self.gui_update_sec)
        self.qtgui_number_sink_0_0.set_update_time(self.gui_update_sec)
        self.qtgui_freq_sink_x_0.set_update_time(self.gui_update_sec)

    def get_gain_rxb(self):
        return self.gain_rxb

    def set_gain_rxb(self, gain_rxb):
        self.gain_rxb = gain_rxb
        self.xmlrpc_client0.set_gain_rxb(self.gain_rxb)

    def get_gain_rxa(self):
        return self.gain_rxa

    def set_gain_rxa(self, gain_rxa):
        self.gain_rxa = gain_rxa
        self.xmlrpc_client1.set_gain_rxa(self.gain_rxa)

    def get_freq_rftune(self):
        return self.freq_rftune

    def set_freq_rftune(self, freq_rftune):
        self.freq_rftune = freq_rftune
        self.xmlrpc_client0_0.set_freq_rftune(self.freq_rftune)

    def get_freq_lo_offset(self):
        return self.freq_lo_offset

    def set_freq_lo_offset(self, freq_lo_offset):
        self.freq_lo_offset = freq_lo_offset
        self.xmlrpc_client0_0_0.set_freq_lo_offset(self.freq_lo_offset)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size
        self.fft_bin_select_B.set_fft_size(self.fft_size)
        self.fft_bin_select_A.set_fft_size(self.fft_size)
        self.blocks_head_0.set_length(self.seconds_record*int(self.samp_rate/self.fft_size))

    def get_client_address(self):
        return self.client_address

    def set_client_address(self, client_address):
        self.client_address = client_address


def main(top_block_cls=holorx_host, options=None):

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
