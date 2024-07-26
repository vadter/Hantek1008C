# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import numpy as np, pylab as pl, sys, os
# import pyhantek
import pyhantek1008C as pyhantek
from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
import multiprocessing as mp
import time

#%% Funcs

def updateGraph(qu1):
   
    plot1 = pg.plot(title = "Plot ADC")
    
    curve1 = plot1.plot([0], [0], pen = pg.mkPen('r', width = 1))
    curve2 = plot1.plot([0], [0], pen = pg.mkPen('g', width = 1))
    curve3 = plot1.plot([0], [0], pen = pg.mkPen('b', width = 1))
    curve4 = plot1.plot([0], [0], pen = pg.mkPen('c', width = 1))
    curve5 = plot1.plot([0], [0], pen = pg.mkPen('m', width = 1))
    curve6 = plot1.plot([0], [0], pen = pg.mkPen('y', width = 1))
    curve7 = plot1.plot([0], [0], pen = pg.mkPen('w', width = 1))
    curve8 = plot1.plot([0], [0], pen = pg.mkPen('r', width = 1))
    
    while True:
        
        Dat = qu1.get()
        
        # curve1.setData(Data[0], Data[1])
        curve1.setData(Dat[0], Dat[1])
        curve2.setData(Dat[0], Dat[2])
        curve3.setData(Dat[0], Dat[3])
        curve4.setData(Dat[0], Dat[4])
        curve5.setData(Dat[0], Dat[5])
        curve6.setData(Dat[0], Dat[6])
        curve7.setData(Dat[0], Dat[7])
        curve8.setData(Dat[0], Dat[8])
        
        QtWidgets.QApplication.processEvents()
        
        time.sleep(0.01)

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

t = 1000. * h0.get_time()

#%% Graph process

que1 = mp.Queue()

graph_process = mp.Process(target = updateGraph, args = (que1,))

graph_process.start()

#%%% Calculations

while True:
    
    Ch1, Ch2, Ch3, Ch4, Ch5, Ch6, Ch7, Ch8 = h0.request_samples_burst_mode()
    
    que1.put((t, Ch1, Ch2, Ch3, Ch4, Ch5, Ch6, Ch7, Ch8))
    
    time.sleep(0.1)

graph_process.join()

h0.close()

#%%%

if __name__ == "__main__":
    
    pass

#%%% End
