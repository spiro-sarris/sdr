#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Path Length Difference
# Author: Spiro Sarris
# Description: Phase and Path Length Difference of Two Receiver Channels
# Generated: Sat Jul 21 14:40:02 2018
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


class demo_length_host(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Path Length Difference")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Path Length Difference")
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

        self.settings = Qt.QSettings("GNU Radio", "demo_length_host")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.velocity_factor = velocity_factor = 0.69
        self.speed_of_light = speed_of_light = 299792458
        self.rf_freq = rf_freq = 100e6
        self.wavelength = wavelength = velocity_factor*speed_of_light/rf_freq
        self.wave_number = wave_number = 2*np.pi/wavelength
        self.meters_per_radian = meters_per_radian = 1/wave_number
        self.variable_qtgui_label_3 = variable_qtgui_label_3 = rf_freq/1e6
        self.variable_qtgui_label_2 = variable_qtgui_label_2 = meters_per_radian
        self.variable_qtgui_label_1 = variable_qtgui_label_1 = wavelength
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = velocity_factor
        self.tx_gain = tx_gain = 30
        self.samp_rate = samp_rate = 100e3
        self.rx_gain = rx_gain = 30
        self.gui_update_sec = gui_update_sec = 0.2
        self.fft_size = fft_size = 64
        self.client_address = client_address = "192.168.10.184"

        ##################################################
        # Blocks
        ##################################################
        self.tabs = Qt.QTabWidget()
        self.tabs_widget_0 = Qt.QWidget()
        self.tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_0)
        self.tabs_grid_layout_0 = Qt.QGridLayout()
        self.tabs_layout_0.addLayout(self.tabs_grid_layout_0)
        self.tabs.addTab(self.tabs_widget_0, 'Magnitude')
        self.tabs_widget_1 = Qt.QWidget()
        self.tabs_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_1)
        self.tabs_grid_layout_1 = Qt.QGridLayout()
        self.tabs_layout_1.addLayout(self.tabs_grid_layout_1)
        self.tabs.addTab(self.tabs_widget_1, 'Phase')
        self.top_grid_layout.addWidget(self.tabs, 0,0,1,2)
        self.zeromq_pull_source_2 = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://192.168.10.184:9997', 100, False, -1)
        self.zeromq_pull_source_1 = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://192.168.10.184:9998', 100, False, -1)
        self.zeromq_pull_source_0 = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://192.168.10.184:9999', 100, False, -1)
        self.xmlrpc_client1 = xmlrpclib.Server('http://192.168.10.184:30000')
        self.xmlrpc_client0 = xmlrpclib.Server('http://192.168.10.184:30000')
        self._variable_qtgui_label_3_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_3_formatter = None
        else:
          self._variable_qtgui_label_3_formatter = lambda x: x
        
        self._variable_qtgui_label_3_tool_bar.addWidget(Qt.QLabel('RF Frequency (MHz)'+": "))
        self._variable_qtgui_label_3_label = Qt.QLabel(str(self._variable_qtgui_label_3_formatter(self.variable_qtgui_label_3)))
        self._variable_qtgui_label_3_tool_bar.addWidget(self._variable_qtgui_label_3_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_3_tool_bar, 1,0,1,1)
          
        self._variable_qtgui_label_2_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_2_formatter = None
        else:
          self._variable_qtgui_label_2_formatter = lambda x: x
        
        self._variable_qtgui_label_2_tool_bar.addWidget(Qt.QLabel('Meters Per Radian of Phase in Cable'+": "))
        self._variable_qtgui_label_2_label = Qt.QLabel(str(self._variable_qtgui_label_2_formatter(self.variable_qtgui_label_2)))
        self._variable_qtgui_label_2_tool_bar.addWidget(self._variable_qtgui_label_2_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_2_tool_bar, 4,0,1,1)
          
        self._variable_qtgui_label_1_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_1_formatter = None
        else:
          self._variable_qtgui_label_1_formatter = lambda x: x
        
        self._variable_qtgui_label_1_tool_bar.addWidget(Qt.QLabel('Wavelength in Cable (m)'+": "))
        self._variable_qtgui_label_1_label = Qt.QLabel(str(self._variable_qtgui_label_1_formatter(self.variable_qtgui_label_1)))
        self._variable_qtgui_label_1_tool_bar.addWidget(self._variable_qtgui_label_1_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_1_tool_bar, 3,0,1,1)
          
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: x
        
        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Velocity Factor of Cable'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_tool_bar, 2,0,1,1)
          
        self._tx_gain_range = Range(0, 40, 1, 30, 50)
        self._tx_gain_win = RangeWidget(self._tx_gain_range, self.set_tx_gain, 'TX Gain', "counter_slider", float)
        self.tabs_grid_layout_0.addWidget(self._tx_gain_win, 1,0,1,1)
        self.to_mag_db_0_4 = to_mag_db()
        self.to_mag_db_0_3 = to_mag_db()
        self.to_mag_db_0_2 = to_mag_db()
        self.to_mag_db_0_1 = to_mag_db()
        self.to_mag_db_0_0 = to_mag_db()
        self.to_mag_db_0 = to_mag_db()
        self._rx_gain_range = Range(0, 30, 1, 30, 100)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, 'RX Gain', "counter_slider", float)
        self.tabs_grid_layout_0.addWidget(self._rx_gain_win, 1,1,1,1)
        self.qtgui_number_sink_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            3
        )
        self.qtgui_number_sink_1.set_update_time(gui_update_sec)
        self.qtgui_number_sink_1.set_title("Length (m)")
        
        labels = ['REF - A', 'REF - B', 'A - B', '', '',
                  '', '', '', '', '']
        units = ['m', 'm', 'm', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(3):
            self.qtgui_number_sink_1.set_min(i, -1)
            self.qtgui_number_sink_1.set_max(i, 1)
            self.qtgui_number_sink_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_1.set_label(i, labels[i])
            self.qtgui_number_sink_1.set_unit(i, units[i])
            self.qtgui_number_sink_1.set_factor(i, factor[i])
        
        self.qtgui_number_sink_1.enable_autoscale(False)
        self._qtgui_number_sink_1_win = sip.wrapinstance(self.qtgui_number_sink_1.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_1.addWidget(self._qtgui_number_sink_1_win, 2,0,1,1)
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            3
        )
        self.qtgui_number_sink_0_0_0.set_update_time(gui_update_sec)
        self.qtgui_number_sink_0_0_0.set_title("Magnitude Difference (dB)")
        
        labels = ['REF - A', 'REF - B', 'A - B', '', '',
                  '', '', '', '', '']
        units = ['dB', 'dB', 'dB', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(3):
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
        self.tabs_grid_layout_0.addWidget(self._qtgui_number_sink_0_0_0_win, 4,0,1,2)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            3
        )
        self.qtgui_number_sink_0_0.set_update_time(gui_update_sec)
        self.qtgui_number_sink_0_0.set_title("Magnitude (dB)")
        
        labels = ['REF', 'RXA', 'RXB', '', '',
                  '', '', '', '', '']
        units = ['dB', 'dB', 'dB', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(3):
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
        self.tabs_grid_layout_0.addWidget(self._qtgui_number_sink_0_0_win, 3,0,1,2)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            3
        )
        self.qtgui_number_sink_0.set_update_time(gui_update_sec)
        self.qtgui_number_sink_0.set_title("Phase Difference (rad)")
        
        labels = ['REF - A', 'REF - B', 'A - B', '', '',
                  '', '', '', '', '']
        units = ['rad', 'rad', 'rad', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(3):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_1.addWidget(self._qtgui_number_sink_0_win, 1,0,1,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_HANN, #wintype
        	rf_freq, #fc
        	samp_rate, #bw
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(gui_update_sec)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, -20)
        self.qtgui_freq_sink_x_0.set_y_label('Amplitude', 'dB')
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
        
        labels = ['REF', 'RXA', 'RXB', '', '',
                  '', '', '', '', '']
        widths = [1, 2, 2, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tabs_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,1,2)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(gui_update_sec)
        self.qtgui_const_sink_x_0.set_y_axis(-4, 4)
        self.qtgui_const_sink_x_0.set_x_axis(-4, 4)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(True)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ['REF - A', 'REF - B', 'A - B', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(3):
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
        self.tabs_grid_layout_1.addWidget(self._qtgui_const_sink_x_0_win, 0,0,1,1)
        self.fft_bin_select_0_1 = fft_bin_select(
            fft_size=64,
            nskip=1,
        )
        self.fft_bin_select_0_0 = fft_bin_select(
            fft_size=64,
            nskip=1,
        )
        self.fft_bin_select_0 = fft_bin_select(
            fft_size=64,
            nskip=1,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_vff((meters_per_radian, ))
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vff((meters_per_radian, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((meters_per_radian, ))
        self.blocks_divide_xx_1_1 = blocks.divide_cc(1)
        self.blocks_divide_xx_1_0 = blocks.divide_cc(1)
        self.blocks_divide_xx_1 = blocks.divide_cc(1)
        self.blocks_complex_to_arg_0_1 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_0 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_add_const_vxx_0_1 = blocks.add_const_vff((np.pi, ))
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((np.pi, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((np.pi, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_1_1, 0))    
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))    
        self.connect((self.blocks_add_const_vxx_0_1, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_add_const_vxx_0_1, 0))    
        self.connect((self.blocks_complex_to_arg_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_complex_to_arg_0_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_complex_to_arg_0_0, 0), (self.qtgui_number_sink_0, 2))    
        self.connect((self.blocks_complex_to_arg_0_1, 0), (self.blocks_add_const_vxx_0_0, 0))    
        self.connect((self.blocks_complex_to_arg_0_1, 0), (self.qtgui_number_sink_0, 1))    
        self.connect((self.blocks_divide_xx_1, 0), (self.blocks_complex_to_arg_0, 0))    
        self.connect((self.blocks_divide_xx_1, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.blocks_divide_xx_1, 0), (self.to_mag_db_0_3, 0))    
        self.connect((self.blocks_divide_xx_1_0, 0), (self.blocks_complex_to_arg_0_1, 0))    
        self.connect((self.blocks_divide_xx_1_0, 0), (self.qtgui_const_sink_x_0, 1))    
        self.connect((self.blocks_divide_xx_1_0, 0), (self.to_mag_db_0_2, 0))    
        self.connect((self.blocks_divide_xx_1_1, 0), (self.blocks_complex_to_arg_0_0, 0))    
        self.connect((self.blocks_divide_xx_1_1, 0), (self.qtgui_const_sink_x_0, 2))    
        self.connect((self.blocks_divide_xx_1_1, 0), (self.to_mag_db_0_4, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_number_sink_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.qtgui_number_sink_1, 1))    
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.qtgui_number_sink_1, 2))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.fft_bin_select_0, 0), (self.blocks_divide_xx_1, 0))    
        self.connect((self.fft_bin_select_0, 0), (self.blocks_divide_xx_1_0, 0))    
        self.connect((self.fft_bin_select_0, 0), (self.to_mag_db_0, 0))    
        self.connect((self.fft_bin_select_0_0, 0), (self.blocks_divide_xx_1, 1))    
        self.connect((self.fft_bin_select_0_0, 0), (self.blocks_divide_xx_1_1, 0))    
        self.connect((self.fft_bin_select_0_0, 0), (self.to_mag_db_0_0, 0))    
        self.connect((self.fft_bin_select_0_1, 0), (self.blocks_divide_xx_1_0, 1))    
        self.connect((self.fft_bin_select_0_1, 0), (self.blocks_divide_xx_1_1, 1))    
        self.connect((self.fft_bin_select_0_1, 0), (self.to_mag_db_0_1, 0))    
        self.connect((self.to_mag_db_0, 0), (self.qtgui_number_sink_0_0, 0))    
        self.connect((self.to_mag_db_0_0, 0), (self.qtgui_number_sink_0_0, 1))    
        self.connect((self.to_mag_db_0_1, 0), (self.qtgui_number_sink_0_0, 2))    
        self.connect((self.to_mag_db_0_2, 0), (self.qtgui_number_sink_0_0_0, 1))    
        self.connect((self.to_mag_db_0_3, 0), (self.qtgui_number_sink_0_0_0, 0))    
        self.connect((self.to_mag_db_0_4, 0), (self.qtgui_number_sink_0_0_0, 2))    
        self.connect((self.zeromq_pull_source_0, 0), (self.fft_bin_select_0_1, 0))    
        self.connect((self.zeromq_pull_source_0, 0), (self.qtgui_freq_sink_x_0, 2))    
        self.connect((self.zeromq_pull_source_1, 0), (self.fft_bin_select_0_0, 0))    
        self.connect((self.zeromq_pull_source_1, 0), (self.qtgui_freq_sink_x_0, 1))    
        self.connect((self.zeromq_pull_source_2, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.zeromq_pull_source_2, 0), (self.fft_bin_select_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "demo_length_host")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_velocity_factor(self):
        return self.velocity_factor

    def set_velocity_factor(self, velocity_factor):
        self.velocity_factor = velocity_factor
        self.set_wavelength(self.velocity_factor*self.speed_of_light/self.rf_freq)
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.velocity_factor))

    def get_speed_of_light(self):
        return self.speed_of_light

    def set_speed_of_light(self, speed_of_light):
        self.speed_of_light = speed_of_light
        self.set_wavelength(self.velocity_factor*self.speed_of_light/self.rf_freq)

    def get_rf_freq(self):
        return self.rf_freq

    def set_rf_freq(self, rf_freq):
        self.rf_freq = rf_freq
        self.set_wavelength(self.velocity_factor*self.speed_of_light/self.rf_freq)
        self.set_variable_qtgui_label_3(self._variable_qtgui_label_3_formatter(self.rf_freq/1e6))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rf_freq, self.samp_rate)

    def get_wavelength(self):
        return self.wavelength

    def set_wavelength(self, wavelength):
        self.wavelength = wavelength
        self.set_wave_number(2*np.pi/self.wavelength)
        self.set_variable_qtgui_label_1(self._variable_qtgui_label_1_formatter(self.wavelength))

    def get_wave_number(self):
        return self.wave_number

    def set_wave_number(self, wave_number):
        self.wave_number = wave_number
        self.set_meters_per_radian(1/self.wave_number)

    def get_meters_per_radian(self):
        return self.meters_per_radian

    def set_meters_per_radian(self, meters_per_radian):
        self.meters_per_radian = meters_per_radian
        self.set_variable_qtgui_label_2(self._variable_qtgui_label_2_formatter(self.meters_per_radian))
        self.blocks_multiply_const_vxx_1_1.set_k((self.meters_per_radian, ))
        self.blocks_multiply_const_vxx_1_0.set_k((self.meters_per_radian, ))
        self.blocks_multiply_const_vxx_1.set_k((self.meters_per_radian, ))

    def get_variable_qtgui_label_3(self):
        return self.variable_qtgui_label_3

    def set_variable_qtgui_label_3(self, variable_qtgui_label_3):
        self.variable_qtgui_label_3 = variable_qtgui_label_3
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_3_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.variable_qtgui_label_3)))

    def get_variable_qtgui_label_2(self):
        return self.variable_qtgui_label_2

    def set_variable_qtgui_label_2(self, variable_qtgui_label_2):
        self.variable_qtgui_label_2 = variable_qtgui_label_2
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_2_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.variable_qtgui_label_2)))

    def get_variable_qtgui_label_1(self):
        return self.variable_qtgui_label_1

    def set_variable_qtgui_label_1(self, variable_qtgui_label_1):
        self.variable_qtgui_label_1 = variable_qtgui_label_1
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_1_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.variable_qtgui_label_1)))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.variable_qtgui_label_0)))

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.xmlrpc_client1.set_tx_gain(self.tx_gain)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rf_freq, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.xmlrpc_client0.set_rx_gain(self.rx_gain)

    def get_gui_update_sec(self):
        return self.gui_update_sec

    def set_gui_update_sec(self, gui_update_sec):
        self.gui_update_sec = gui_update_sec
        self.qtgui_number_sink_1.set_update_time(self.gui_update_sec)
        self.qtgui_number_sink_0_0_0.set_update_time(self.gui_update_sec)
        self.qtgui_number_sink_0_0.set_update_time(self.gui_update_sec)
        self.qtgui_number_sink_0.set_update_time(self.gui_update_sec)
        self.qtgui_freq_sink_x_0.set_update_time(self.gui_update_sec)
        self.qtgui_const_sink_x_0.set_update_time(self.gui_update_sec)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_client_address(self):
        return self.client_address

    def set_client_address(self, client_address):
        self.client_address = client_address


def main(top_block_cls=demo_length_host, options=None):

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
