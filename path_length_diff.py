#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Path Length Difference
# Author: Spiro Sarris
# Description: Phase and Path Length Difference of Two Receiver Channels
# Generated: Sun Jul  8 19:09:48 2018
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy as np
import sip
import sys


class path_length_diff(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "path_length_diff")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.wf_freq = wf_freq = 100
        self.speed_of_light = speed_of_light = 100
        self.wavelength = wavelength = speed_of_light/wf_freq
        self.wave_number = wave_number = np.pi/wavelength
        self.velocity_factor = velocity_factor = 1
        self.samp_rate = samp_rate = 10e3

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	int(samp_rate/wf_freq), #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
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
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_number_sink_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_1.set_update_time(0.10)
        self.qtgui_number_sink_1.set_title("Length Difference (m)")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
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
        self.top_layout.addWidget(self._qtgui_number_sink_1_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.2)
        self.qtgui_number_sink_0.set_title("Phase Difference (rad)")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
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
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, int(samp_rate/wf_freq/4))
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_arg_0_0 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, wf_freq, 1, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, wave_number)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_divide_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_sub_xx_0, 0))    
        self.connect((self.blocks_complex_to_arg_0_0, 0), (self.blocks_sub_xx_0, 1))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_complex_to_arg_0_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.qtgui_number_sink_1, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_divide_xx_0, 0))    
        self.connect((self.blocks_sub_xx_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_arg_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_real_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "path_length_diff")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_wf_freq(self):
        return self.wf_freq

    def set_wf_freq(self, wf_freq):
        self.wf_freq = wf_freq
        self.set_wavelength(self.speed_of_light/self.wf_freq)
        self.blocks_delay_0.set_dly(int(self.samp_rate/self.wf_freq/4))
        self.analog_sig_source_x_0.set_frequency(self.wf_freq)

    def get_speed_of_light(self):
        return self.speed_of_light

    def set_speed_of_light(self, speed_of_light):
        self.speed_of_light = speed_of_light
        self.set_wavelength(self.speed_of_light/self.wf_freq)

    def get_wavelength(self):
        return self.wavelength

    def set_wavelength(self, wavelength):
        self.wavelength = wavelength
        self.set_wave_number(np.pi/self.wavelength)

    def get_wave_number(self):
        return self.wave_number

    def set_wave_number(self, wave_number):
        self.wave_number = wave_number
        self.analog_const_source_x_0.set_offset(self.wave_number)

    def get_velocity_factor(self):
        return self.velocity_factor

    def set_velocity_factor(self, velocity_factor):
        self.velocity_factor = velocity_factor

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_delay_0.set_dly(int(self.samp_rate/self.wf_freq/4))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)


def main(top_block_cls=path_length_diff, options=None):

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
