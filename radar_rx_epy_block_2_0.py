"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
from gnuradio import gr
import numpy as np
from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog

from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from xmlrpc.client import ServerProxy
import threading


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, freq='Initialising'):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Trigger Test2',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.freq = freq

        self.xmlrpc_client_0 = ServerProxy('http://'+'localhost'+':8080')    

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def work(self, input_items, output_items):

        output_items[0][:]=input_items[0]
        var=(output_items[0])
        state0 ='No Target Detected'
        state1= 'Target Detected'
        state=''
        if(any(var)==True):
            state=state1
            self.freq=state1
           # playsound.playsound('1.mp3')
        if(any(var)==False):
            state=state0
            self.freq=state0
            #pysine.sine(frequency=440.0, duration=1.0)
        self.xmlrpc_client_0.set_freq(self.freq)
        return len(input_items[0])
