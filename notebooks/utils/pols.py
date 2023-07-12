# -*- coding: utf-8 -*-
#
#       Copyright 2022
#       Maximiliano Isi <max.isi@ligo.org>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import numpy as np

# linear basis tensors
ep = np.array([[1, 0], [0, -1]])
ec = np.array([[0, 1], [1, 0]])

def hphc_ellip(wt, A=0.2, ellip=1, theta=0):
    """Returns the plus and cross polarization states corresponding to 
    a given set of polarization ellipse parameters (assuming no initial phase).
    """
    coswt = np.cos(wt)
    sinwt = np.sin(wt)
    hp = coswt*np.cos(theta) - ellip*sinwt*np.sin(theta)
    hc = coswt*np.sin(theta) + ellip*sinwt*np.cos(theta)
    return A*hp, A*hc

def dxdy_ellip(XY, *args, **kwargs):
    """Returns the displacement vectors produced by a given elliptical GW.
    """
    hp, hc = hphc_ellip(*args, **kwargs)
    return np.dot(hp*ep + hc*ec, XY)