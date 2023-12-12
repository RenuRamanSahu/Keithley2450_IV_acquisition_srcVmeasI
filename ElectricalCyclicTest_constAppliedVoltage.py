# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:49:19 2023

@author: LANSPE_OPTICS
"""

import numpy as np
import matplotlib.pyplot as plt
from pymeasure.instruments.keithley import Keithley2450
from pymeasure.instruments import *
from time import sleep, time


#############################
sleepTime = 0.02 #time in second, manual time delay after a measurement
filename = "alwar"
appliedVoltage = 0.01

#Use CTRL+C in the console to stop the program. 
#Data is stored in the folder where the program is running.


# resources = list_resources()    Run this to know the USB port the instrument is connected to
#Connect and configure the instrument
#sm stands for sourcemeter

sm = Keithley2450("USB0::0x05E6::0x2450::04459144::INSTR")


#reset the sourcemeter 
sm.reset()

sm.use_front_terminals()
sm.apply_voltage()
sm.measure_current()
sm.enable_source()

#wait to give time for the instrument to react
sleep(1)


f = open(filename+".txt", "w")
f.write("#Time(s)  Voltage(V)  Current(A)   Resistance(Ohm)\n")
f.close()


timeStart = time()
while(1):
    sm.start_buffer()
    sm.source_voltage = appliedVoltage
    sleep(sleepTime)
    
    #record the average voltage and standard deviation
    time_now = np.round(time()-timeStart, decimals = 2)
    I = sm.current
    V = sm.source_voltage
    R = V/I
    
    content =  str(time_now)+"   "+str(I)+"   "+str(V)+"   "+str(R)+"\n"
    content1 = ("I = "+str(I)+" V = "+str(V)+" R = V/I = "+str(R) )
    f = open(filename+".txt", "a")
    f.write(content)
    f.close()
    
    
    print("Time Elapsed (s) = "+ str(time_now)+"  "+content1)

    















