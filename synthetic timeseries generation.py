# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 00:27:24 2024

@author: sp825
"""
import os
import pandas as pf
import numpy as np
from pyswmm import Simulation, Nodes, Links, Subcatchments, RainGages

import datetime
import xlsxwriter


""" 现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码； """
""" 现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码； """
""" 现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码； """



""" 现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码； """
""" 现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码； """
""" 现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码； """



""" 现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码； """
""" 现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码； """
""" 现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码；现在开始切割一下代码； """

control_time_step = 300 
# The file "Astlingen_SWMM_BC.inp" is acquired from https://github.com/open-toolbox/SWMM-Astlingen.


swmm_inp = "Astlingen_SWMM_BC.inp"

CSO_time = []  
    
with Simulation(swmm_inp) as sim:
    print("start time", sim.start_time)
    print("end time", sim.end_time)
        
    sim.step_advance(control_time_step)
    
    
    # init node object, link object, and subcatchment object
    subcatchment_object = Subcatchments(sim)
    SC01 = subcatchment_object["SC01"]
    SC02 = subcatchment_object["SC02"]
    SC03 = subcatchment_object["SC03"]
    SC04 = subcatchment_object["SC04"]
    SC05 = subcatchment_object["SC05"]
    SC06 = subcatchment_object["SC06"]
    SC07 = subcatchment_object["SC07"]
    SC08 = subcatchment_object["SC08"]
    SC09 = subcatchment_object["SC09"]
    SC010 = subcatchment_object["SC010"]
    
    node_object = Nodes(sim)  # init node object
    T1 = node_object["T1"]
    T2 = node_object["T2"]
    T3 = node_object["T3"]
    T4 = node_object["T4"]
    T5 = node_object["T5"]
    T6 = node_object["T6"]
    CSO7 = node_object["CSO7"]
    CSO8 = node_object["CSO8"]
    CSO9 = node_object["CSO9"]
    CSO10 = node_object["CSO10"]
    J1 = node_object["J1"]
    J2 = node_object["J2"]
    J3 = node_object["J3"]
    J4 = node_object["J4"]
    J5 = node_object["J5"]
    J6 = node_object["J6"]
    J7 = node_object["J7"]
    J8 = node_object["J8"]
    J9 = node_object["J9"]
    J10 = node_object["J10"]
    J11 = node_object["J11"]
    J12 = node_object["J12"]
    J13 = node_object["J13"]
    J14 = node_object["J14"]
    J15 = node_object["J15"]
    J16 = node_object["J16"]
    J17 = node_object["J17"]
    J18 = node_object["J18"]
    J19 = node_object["J19"]
    Out_to_WWTP = node_object["Out_to_WWTP"]
    
    link_object = Links(sim)  # init link object
    C14 = link_object["C14"]
    V1 = link_object["V1"]
    V2 = link_object["V2"]
    V3 = link_object["V3"]
    V4 = link_object["V4"]
    V5 = link_object["V5"]
    V6 = link_object["V6"]
    
    raingage_object = RainGages(sim) # init rain gages object
    RG1 = raingage_object["RG1"]
    RG2 = raingage_object["RG2"]
    RG3 = raingage_object["RG3"]
    RG4 = raingage_object["RG4"]
    

    for step in sim:
        if T1.flooding > 0 or T2.flooding > 0 or T3.flooding > 0 or T4.flooding > 0 or T5.flooding > 0 or T6.flooding > 0 or CSO7.flooding > 0 or CSO8.flooding > 0 or CSO9.flooding > 0 or CSO10.flooding > 0:
            
            CSO_time.append(sim.current_time)
        pass


   
CSO_start_time = datetime.datetime(2000,1,1,0,0,0)
CSO_end_time = datetime.datetime(2000,12,31,23,55,0)

START = []
Start_order = []
for m in range (len(CSO_time)):
    if m == 0:
        if (CSO_time[m] - CSO_start_time).total_seconds() > 36000:
            time_start = CSO_time[m] - datetime.timedelta(hours=10)
            START.append(time_start) 
        else:
            START.append(CSO_start_time)
        
    else:
        if (CSO_time[m] - CSO_time[m-1]).total_seconds() > 72000:
            time_start = CSO_time[m] - datetime.timedelta(hours=10)
            START.append(time_start) 
            
            Start_order.append(m)


End_order = []
for n in range (len(Start_order)):
    End_order.append(Start_order[n] -1)



END = []
for i in range (len(End_order)):
    end_order = End_order[i]
    time_end = CSO_time[end_order] + datetime.timedelta(hours=10)
    END.append(time_end)
    
    
# print(End_order)
CSO_end_time = CSO_time[-1] + datetime.timedelta(hours=10)
END.append(CSO_end_time)
# print(CSO_end_time)

print(len(START), len(END))

bbb = 0
for j in range (len(START)):
    ccc = (END[j] - START[j]).total_seconds()/control_time_step
    bbb = bbb + ccc
    
    
print("total_steps", bbb)
        






# Next, generate synthetic rainfall data
print("++++++++++++ synthetic timeseries +++++++++++++++")


# some functions for rain data extraction (for training events or testing events)
# --------------------------------------------------------------------------------
def Timestep_Attribute(Start_date, Start_time, End_date, End_time, Current_date, Current_time, timestep_attribute):
    
    if timestep_attribute == 0:
        # comparison between Start and Current
        if Start_date == Current_date and Start_time == Current_time:
            new_timestep_attribute = 1
        else:
            new_timestep_attribute = 0
            
    if timestep_attribute == 1:
        # comparison between End and Current
        if End_date == Current_date and End_time == Current_time:
            new_timestep_attribute = 2
        else:
            new_timestep_attribute = 1
            
    if timestep_attribute == 2 or timestep_attribute == 3:
        new_timestep_attribute = 3
    
    
    return new_timestep_attribute


def rainfall_data_each_raingage(Data_RaGe, Start_date, Start_time, End_date, End_time):
    One_raingage_rainfall_data = []
        
    timestep_attribute = 0
    with open(Data_RaGe, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip('\n')  
            line_rain = line.split()
            Current_date, Current_time = line_rain[0], line_rain[1]
            
            timestep_attribute = Timestep_Attribute(Start_date, Start_time, End_date, End_time, Current_date, Current_time, timestep_attribute)
            if timestep_attribute == 1 or timestep_attribute == 2:
                One_raingage_rainfall_data.append(float(line_rain[2]))
    
    return One_raingage_rainfall_data


def rainfall_data_extraction(Start_date, Start_time, End_date, End_time):
    Rainfall_path = "E:/Astlingen2000_network capacity analysis/"
    Data_RG1_file = Rainfall_path + "1Astlingen_Erft1.txt"
    SaveList_RG1 = rainfall_data_each_raingage(Data_RG1_file, Start_date, Start_time, End_date, End_time)
    
    Data_RG2_file = Rainfall_path + "2Astlingen_Erft2.txt"
    SaveList_RG2 = rainfall_data_each_raingage(Data_RG2_file, Start_date, Start_time, End_date, End_time)
    
    Data_RG3_file = Rainfall_path + "3Astlingen_Erft3.txt"
    SaveList_RG3 = rainfall_data_each_raingage(Data_RG3_file, Start_date, Start_time, End_date, End_time)
    
    Data_RG4_file = Rainfall_path + "4Astlingen_Erft4.txt"
    SaveList_RG4 = rainfall_data_each_raingage(Data_RG4_file, Start_date, Start_time, End_date, End_time)
    
    
    return SaveList_RG1, SaveList_RG2, SaveList_RG3, SaveList_RG4
    
def str_to_datetime(str_date, str_time):
    year = int(str_date[6:])
    month = 10*int(str_date[0]) + int(str_date[1])
    day = 10*int(str_date[3]) + int(str_date[4])

    hour = 10*int(str_time[0]) + int(str_time[1])
    minute = 10*int(str_time[3]) + int(str_time[4])
    second = 10*int(str_time[6]) + int(str_time[7])
    
    return [year, month, day, hour, minute, second]





# global data extraction, including rainfall data and simulation start time and end time
# --------------------------------------------------------------------------------



Synthetic_Rainfall_RG1, Synthetic_Rainfall_RG2, Synthetic_Rainfall_RG3, Synthetic_Rainfall_RG4 = [], [], [], []


for j in range (len(START)):
    str_start_date = str(START[j].date().strftime('%m/%d/%Y'))
    str_start_time = str(START[j].time().strftime('%H:%M:%S'))
    str_end_date = str(END[j].date().strftime('%m/%d/%Y'))
    str_end_time = str(END[j].time().strftime('%H:%M:%S'))
    savelist_RG1, savelist_RG2, savelist_RG3, savelist_RG4 = rainfall_data_extraction(str_start_date, str_start_time, str_end_date, str_end_time)

    for k in range (len(savelist_RG1)):
        Synthetic_Rainfall_RG1.append(savelist_RG1[k])
        Synthetic_Rainfall_RG2.append(savelist_RG2[k])
        Synthetic_Rainfall_RG3.append(savelist_RG3[k])
        Synthetic_Rainfall_RG4.append(savelist_RG4[k])

    

print(len(Synthetic_Rainfall_RG1))



length = len(Synthetic_Rainfall_RG1)




Synthetic_time = []     
synthetic_start = datetime.datetime(2000, 1, 1, 0, 0, 0)
step = datetime.timedelta(minutes=5)

STR_DATE = []
STR_TIME = []
print("===============time===============")

for mmm in range (length):
    if mmm == 0:
        synthetic_current = synthetic_start
        Synthetic_time.append(synthetic_current)
    else:
        synthetic_current = synthetic_current + step
        Synthetic_time.append(synthetic_current)
    str_date = datetime.datetime.strftime(synthetic_current,'%m/%d/%Y')
    str_time = datetime.datetime.strftime(synthetic_current,'%H:%M:%S')
    
    STR_DATE.append(str_date)
    STR_TIME.append(str_time)
    # print(synthetic_current, "date", str_date, "time", str_time)

with open(r'RG1_synthetic_year2000.txt', 'w') as f:
    for i in range (length):
        f.write(STR_DATE[i] + ' ' + STR_TIME[i] + ' ' + str(Synthetic_Rainfall_RG1[i]) +  '\n')
        
with open(r'RG2_synthetic_year2000.txt', 'w') as f:
    for i in range (length):
        f.write(STR_DATE[i] + ' ' + STR_TIME[i] + ' ' + str(Synthetic_Rainfall_RG2[i]) +  '\n')

with open(r'RG3_synthetic_year2000.txt', 'w') as f:
    for i in range (length):
        f.write(STR_DATE[i] + ' ' + STR_TIME[i] + ' ' + str(Synthetic_Rainfall_RG3[i]) +  '\n')

with open(r'RG4_synthetic_year2000.txt', 'w') as f:
    for i in range (length):
        f.write(STR_DATE[i] + ' ' + STR_TIME[i] + ' ' + str(Synthetic_Rainfall_RG4[i]) +  '\n')


