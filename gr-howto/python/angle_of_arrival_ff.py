#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Spiro Sarris.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#


import numpy as np
from gnuradio import gr

class angle_of_arrival_ff(gr.sync_block):
    """
    Calculates the angle of arrival from the phase difference of the two signals
    as AoA = A1*(numpy.arccos(delta_phase / (k * D))) + A0
    @param k: Spatial Frequency of wave [radians / meter]
    @param D: Separation Distance between antenna elements [m]
    @param A1 (optional): Multiply calculated result by constant (example: convert radians to degrees) 
    @param A0 (optional): Add constant to result (example: rotate origin of angle coordinate)
    """
    def __init__(self, k, D, A1=1, A0=0):
        self.k = k
        self.D = D
        self.A1 = A1
        self.A0 = A0
        gr.sync_block.__init__(self,
            name="angle_of_arrival_ff",
            in_sig=[np.float32],
            out_sig=[np.float32])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = self.A1*(np.arccos(in0 / (self.k * self.D))) + self.A0
        return len(output_items[0])

