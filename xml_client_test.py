#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: raidfire
# GNU Radio version: 3.10.4.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
import sip
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import network
from gnuradio.qtgui import Range, GrRangeWidget
from PyQt5 import QtCore
from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer
import threading
import xml_client_test_epy_block_2_0 as epy_block_2_0  # embedded python block



from gnuradio import qtgui

class xml_client_test(gr.top_block, Qt.QWidget):

    def __init__(self, freq='Initialising', ip='192.168.1.104'):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "xml_client_test")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq
        self.ip = ip

        ##################################################
        # Variables
        ##################################################
        self.threshr = threshr = 175
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = freq
        self.threshp = threshp = threshr
        self.samp_rate = samp_rate = 1000000

        ##################################################
        # Blocks
        ##################################################
        self.xmlrpc_server_1 = SimpleXMLRPCServer(('localhost', 8080), allow_none=True)
        self.xmlrpc_server_1.register_instance(self)
        self.xmlrpc_server_1_thread = threading.Thread(target=self.xmlrpc_server_1.serve_forever)
        self.xmlrpc_server_1_thread.daemon = True
        self.xmlrpc_server_1_thread.start()
        self.xmlrpc_client_0_0_0_0 = ServerProxy('http://'+ip+':6005')
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
            self._variable_qtgui_label_0_formatter = None
        else:
            self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel("Detection Status"))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_tool_bar)
        self._threshr_range = Range(0, 1000, 1, 175, 200)
        self._threshr_win = GrRangeWidget(self._threshr_range, self.set_threshr, "Detection Threshold", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._threshr_win)
        self.qtgui_number_sink_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1,
            None # parent
        )
        self.qtgui_number_sink_1.set_update_time(0.5)
        self.qtgui_number_sink_1.set_title("STATE")

        labels = ['Detect', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_1.set_min(i, 0)
            self.qtgui_number_sink_1.set_max(i, 1)
            self.qtgui_number_sink_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_1.set_label(i, labels[i])
            self.qtgui_number_sink_1.set_unit(i, units[i])
            self.qtgui_number_sink_1.set_factor(i, factor[i])

        self.qtgui_number_sink_1.enable_autoscale(False)
        self._qtgui_number_sink_1_win = sip.wrapinstance(self.qtgui_number_sink_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_1_win)
        self.network_tcp_source_2_0 = network.tcp_source.tcp_source(itemsize=gr.sizeof_float*1,addr=ip,port=6001,server=False)
        self.epy_block_2_0 = epy_block_2_0.blk(freq=1.0)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_1, 0), (self.epy_block_2_0, 0))
        self.connect((self.epy_block_2_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.epy_block_2_0, 0), (self.qtgui_number_sink_1, 0))
        self.connect((self.network_tcp_source_2_0, 0), (self.blocks_throttle_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "xml_client_test")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_variable_qtgui_label_0(self.freq)

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        self.ip = ip

    def get_threshr(self):
        return self.threshr

    def set_threshr(self, threshr):
        self.threshr = threshr
        self.set_threshp(self.threshr)

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0))))

    def get_threshp(self):
        return self.threshp

    def set_threshp(self, threshp):
        self.threshp = threshp
        self.xmlrpc_client_0_0_0_0.set_threshp(self.threshp)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--freq", dest="freq", type=str, default='Initialising',
        help="Set freq [default=%(default)r]")
    parser.add_argument(
        "--ip", dest="ip", type=str, default='192.168.1.104',
        help="Set ip [default=%(default)r]")
    return parser


def main(top_block_cls=xml_client_test, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(freq=options.freq, ip=options.ip)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
