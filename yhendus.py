#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import os
import time
import datetime

seisuaeg = 0
poolLahtiMinekuAeg = 10 #sekundites

def saadaArduinole (sonum):
    if len(sonum)<2:
        errorLog = open("error.log", "a")
        errorLog.write("aeg: " + str(datetime.datetime.now()) + " ERROR: arduinole saadetakse illegaalse sonumi: " + sonum + '\n')
        errorLog.close()
    else:
        link.write(sonum)
        print sonum
    tagasi = link.readline()
    algAeg = int(time.time())
    while len(tagasi)<2:
        tagasi = link.readline()
        if time.time() > (algAeg + 3):
             errorLog = open("error.log", "a")
             errorLog.write("aeg: " + str(datetime.datetime.now()) + " ERROR: arduino ei saatnud tagasi sonumit 3 seki jooksul, kask" + '\n')
             errorLog.close()
             break
    if tagasi == "LDERROR":
        errorLog = open("error.log", "a")
        errorLog.write("aeg: " + str(datetime.datetime.now()) + " ERROR: arduino kurdab et sai illegaalse sonumi: " + tagasi + '\n')
        errorLog.close()

#try:
print "Init serial"
link = serial.Serial('/dev/arduino',9600,timeout=5)
print "Yes serial"
#except:
#    print "No serial"
while 1:
    while (os.stat("buffer.txt").st_size == 0):
        if (seisuaeg - time.time()) < 0 and seisuaeg != 0:
            saadaArduinole("LDST")
            seisuaeg = 0
                            
        time.sleep(1)
    buffer = open("buffer.txt","r")
    kerimine = buffer.readline().strip()
    suund = buffer.readline().strip()
    buffer.close()
    f = open("buffer.txt", "w")
    f.close()

    sonum = ""
    if suund == "stopp":
        sonum = "LDST"
    elif suund == "kinni":
        sonum = "LDKI"
    elif suund == "lahti":
        sonum = "LDLA"
    elif kerimine == "olek":
        olekuFail = open("olek.txt", "w")
        olekuFail.write(str(datetime.datetime.now()) + "\n")
        link.write("OL")
        print "OL"
        saadudOlek = link.readline()
        algAeg = time.time()
        while len(saadudOlek)<2:
            saadudOlek = link.readline()
            if time.time() > (algAeg + 3):
                 errorLog = open("error.log", "a")
                 errorLog.write("aeg: " + str(datetime.datetime.now()) + " ERROR: arduino ei saatnud tagasi sonumit 3 seki jooksul, kask" + '\n')
                 errorLog.close()
                 break
        if saadudOlek[2] == 'S':
            olekuFail.write("sulgub" + '\n')
        elif saadudOlek[2] == 'A':
            olekuFail.write("avaneb" + '\n')
        elif saadudOlek[2] == 'N':
            olekuFail.write("seisab" + '\n')
        else:
            errorLog = open("error.log", "a")
            errorLog.write("aeg: " + str(datetime.datetime.now()) + " ERROR: illegaalne olek arduinolt: " + saadudOlek + '\n')
            errorLog.close()
        olekuFail.write(str(saadudOlek[3]) + ',' + str(saadudOlek[4]) + str(saadudOlek[5]) + '\n')
        olekuFail.write(saadudOlek)
        olekuFail.close()
    else:
        errorLog = open("error.log", "a")
        errorLog.write("aeg: " + str(datetime.datetime.now()) + " ERROR: illegaalne suund: " + suund + '\n')
        errorLog.close()

    if kerimine == "pooleldi":
        seisuaeg = int(time.time()) + poolLahtiMinekuAeg

    if len(sonum)>2:
        saadaArduinole(sonum)
    