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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from angle_of_arrival_ff import angle_of_arrival_ff
import numpy as np

class qa_angle_of_arrival_ff(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_001_angle_of_arrival_ff (self):
        src_data = (-1, 0, 1)
        expected_result = (np.pi, 0.5*np.pi, 0)
        src = blocks.vector_source_f (src_data)
        sqr = angle_of_arrival_ff (1, 2, 3, 4)
        dst = blocks.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)


if __name__ == '__main__':
    gr_unittest.run(qa_angle_of_arrival_ff)
