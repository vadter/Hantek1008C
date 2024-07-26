# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import numpy as np, pylab as pl, sys, os, time
# import pyhantek
import pyhantek1008C as pyhantek

ll = ['/home/vadter/.local/bin']

if (sys.path.count(ll) == 0):

    sys.path = sys.path + ll

import optelems3 as oe

#%% Settings

ChVDIV = [1., 1., 1., 1., 1., 1., 1., 1.] # V / Div # 0.125, 0.02

#%% Apply settings

# t0 = time.time()

h0 = pyhantek.Hantek1008CRaw(ns_per_div = 100_000,
                             vertical_scale_factor = ChVDIV,
             				 active_channels = None,
             				 trigger_channel = 0,
             				 trigger_slope = "rising",
             				 trigger_level = 2048)

# dt = time.time() - t0
# print('h0 in %1.3f s' % (dt))

# h0.connect()

# dt = time.time() - t0
# print('h0.connect() in %1.3f s' % (dt))

# h0.init()

# ChsData = h0.request_samples_burst_mode()

# dt = time.time() - t0
# print('Data in %1.3f s' % (dt))

#%% Calculations

t = 1000. * h0.get_time() # ms

Ch1, Ch2, Ch3, Ch4, Ch5, Ch6, Ch7, Ch8 = h0.request_samples_burst_mode()

# t = t[0:Ch1.size]

#%%

h0.close()

#%% Graphics

# pl.figure()

# pl.plot(ChsData[0], '-or', label = 'Ch1')

# pl.legend()

# pl.grid(True)

# oe.CoordsToConsol()

pl.figure()

# Ch1

pl.subplot(241)

pl.plot(t, Ch1, 'r', label = 'Ch1')

pl.ylim([-10. * ChVDIV[0], 10. * ChVDIV[0]])

pl.legend()

pl.grid(True)

pl.xlabel('Time, ms')
pl.ylabel('U, Volts')

# Ch2

pl.subplot(242)

pl.plot(t, Ch2, 'g', label = 'Ch2')

pl.ylim([-10. * ChVDIV[1], 10. * ChVDIV[1]])

pl.legend()

pl.grid(True)

pl.xlabel('Time, ms')
pl.ylabel('U, Volts')

# Ch3

pl.subplot(243)

pl.plot(t, Ch3, 'b', label = 'Ch2')

pl.ylim([-10. * ChVDIV[2], 10. * ChVDIV[2]])

pl.legend()

pl.grid(True)

pl.xlabel('Time, ms')
pl.ylabel('U, Volts')

# Ch4

pl.subplot(244)

pl.plot(t, Ch3, 'c', label = 'Ch4')

pl.ylim([-10. * ChVDIV[3], 10. * ChVDIV[3]])

pl.legend()

pl.grid(True)

pl.xlabel('Time, ms')
pl.ylabel('U, Volts')

# Ch5

pl.subplot(245)

pl.plot(t, Ch5, 'm', label = 'Ch5')

pl.ylim([-10. * ChVDIV[4], 10. * ChVDIV[4]])

pl.legend()

pl.grid(True)

pl.xlabel('Time, ms')
pl.ylabel('U, Volts')

# Ch6

pl.subplot(246)

pl.plot(t, Ch6, 'y', label = 'Ch6')

pl.ylim([-10. * ChVDIV[5], 10. * ChVDIV[5]])

pl.legend()

pl.grid(True)

pl.xlabel('Time, ms')
pl.ylabel('U, Volts')

# Ch7

pl.subplot(247)

pl.plot(t, Ch7, 'k', label = 'Ch7')

pl.ylim([-10. * ChVDIV[6], 10. * ChVDIV[6]])

pl.legend()

pl.grid(True)

pl.xlabel('Time, ms')
pl.ylabel('U, Volts')

pl.subplot(248)

pl.plot(t, Ch8, 'k', label = 'Ch8')

pl.ylim([-10. * ChVDIV[7], 10. * ChVDIV[7]])

pl.legend()

pl.grid(True)

pl.xlabel('Time, ms')
pl.ylabel('U, Volts')

oe.CoordsToConsol()

pl.show()

#%%%

if __name__ == "__main__":
    
    pass

#%%% End