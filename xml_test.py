#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: raidfire
# GNU Radio version: 3.10.4.0

from gnuradio import analog
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import iio
from gnuradio import network
from xmlrpc.server import SimpleXMLRPCServer
import threading




class xml_test(gr.top_block):

    def __init__(self, f1p=131001, gainp=0, lop=4200000000, rfp=0, samp_rate=1000000, testp='0', threshp=0):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)

        ##################################################
        # Parameters
        ##################################################
        self.f1p = f1p
        self.gainp = gainp
        self.lop = lop
        self.rfp = rfp
        self.samp_rate = samp_rate
        self.testp = testp
        self.threshp = threshp

        ##################################################
        # Variables
        ##################################################
        self.fft_size = fft_size = 512
        self.decim = decim = 1024

        ##################################################
        # Blocks
        ##################################################
        self.xmlrpc_server_0 = SimpleXMLRPCServer(('127.0.0.1', 6005), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.network_tcp_sink_3 = network.tcp_sink(gr.sizeof_float, 1, '127.0.0.1', 6001,2)
        self.iio_pluto_source_0 = iio.fmcomms2_source_fc32('ip:192.168.2.1' if 'ip:192.168.2.1' else iio.get_pluto_uri(), [True, True], 32768)
        self.iio_pluto_source_0.set_len_tag_key('packet_len')
        self.iio_pluto_source_0.set_frequency(lop)
        self.iio_pluto_source_0.set_samplerate(samp_rate)
        self.iio_pluto_source_0.set_gain_mode(0, 'manual')
        self.iio_pluto_source_0.set_gain(0, gainp)
        self.iio_pluto_source_0.set_quadrature(True)
        self.iio_pluto_source_0.set_rfdc(True)
        self.iio_pluto_source_0.set_bbdc(True)
        self.iio_pluto_source_0.set_filter_params('Auto', '', 0, 0)
        self.iio_pluto_sink_1 = iio.fmcomms2_sink_fc32('ip:192.168.2.1' if 'ip:192.168.2.1' else iio.get_pluto_uri(), [True, True], 32768, False)
        self.iio_pluto_sink_1.set_len_tag_key('')
        self.iio_pluto_sink_1.set_bandwidth(20000000)
        self.iio_pluto_sink_1.set_frequency(lop)
        self.iio_pluto_sink_1.set_samplerate(samp_rate)
        self.iio_pluto_sink_1.set_attenuation(0, 0)
        self.iio_pluto_sink_1.set_filter_params('Auto', '', 0, 0)
        self.fft_vxx_0_0_0_1 = fft.fft_vcc(fft_size, True, window.blackmanharris(fft_size), False, 8)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, fft_size)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(fft_size)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 10000, 1, 0.01, 0)
        self.analog_agc_xx_0_0 = analog.agc_cc((1e-4), 1.0, 1.0)
        self.analog_agc_xx_0_0.set_max_gain(65536)
        self.analog_agc_xx_0 = analog.agc_cc((1e-4), 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(65536)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.analog_agc_xx_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.iio_pluto_sink_1, 0))
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.fft_vxx_0_0_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.network_tcp_sink_3, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.fft_vxx_0_0_0_1, 0), (self.blocks_complex_to_mag_0_0, 0))
        self.connect((self.iio_pluto_source_0, 0), (self.analog_agc_xx_0_0, 0))


    def get_f1p(self):
        return self.f1p

    def set_f1p(self, f1p):
        self.f1p = f1p

    def get_gainp(self):
        return self.gainp

    def set_gainp(self, gainp):
        self.gainp = gainp
        self.iio_pluto_source_0.set_gain(0, self.gainp)

    def get_lop(self):
        return self.lop

    def set_lop(self, lop):
        self.lop = lop
        self.iio_pluto_sink_1.set_frequency(self.lop)
        self.iio_pluto_source_0.set_frequency(self.lop)

    def get_rfp(self):
        return self.rfp

    def set_rfp(self, rfp):
        self.rfp = rfp

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.iio_pluto_sink_1.set_samplerate(self.samp_rate)
        self.iio_pluto_source_0.set_samplerate(self.samp_rate)

    def get_testp(self):
        return self.testp

    def set_testp(self, testp):
        self.testp = testp

    def get_threshp(self):
        return self.threshp

    def set_threshp(self, threshp):
        self.threshp = threshp

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--f1p", dest="f1p", type=eng_float, default=eng_notation.num_to_str(float(131001)),
        help="Set f1p [default=%(default)r]")
    parser.add_argument(
        "--gainp", dest="gainp", type=intx, default=0,
        help="Set gainp [default=%(default)r]")
    parser.add_argument(
        "--lop", dest="lop", type=intx, default=4200000000,
        help="Set lop [default=%(default)r]")
    parser.add_argument(
        "--rfp", dest="rfp", type=intx, default=0,
        help="Set rfp [default=%(default)r]")
    parser.add_argument(
        "--samp-rate", dest="samp_rate", type=intx, default=1000000,
        help="Set samp_rate [default=%(default)r]")
    parser.add_argument(
        "--testp", dest="testp", type=str, default='0',
        help="Set testp [default=%(default)r]")
    parser.add_argument(
        "--threshp", dest="threshp", type=intx, default=0,
        help="Set threshp [default=%(default)r]")
    return parser


def main(top_block_cls=xml_test, options=None):
    if options is None:
        options = argument_parser().parse_args()
    tb = top_block_cls(f1p=options.f1p, gainp=options.gainp, lop=options.lop, rfp=options.rfp, samp_rate=options.samp_rate, testp=options.testp, threshp=options.threshp)

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
