## Libraries
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk

import pyvisa
from ThorlabsPM100 import ThorlabsPM100
import matplotlib.pyplot as plt
import time

## Functions & Start

def ConfigurePower():
    power_meter.configure.scalar.power()
    Unit=" W"
    Display.config(text=str(power_meter.read)+Unit)

def ConfigureCurrent():
    power_meter.configure.scalar.current.dc()
    Unit=" A"
    Display.config(text=str(power_meter.read)+Unit)

def ConfigureLambda():
    Lambda=entryLambda.get()
    power_meter.sense.correction.wavelength = int(Lambda)

if __name__ == "__main__":

    #Initialisation
    global rm, inst, power_meter
    rm = pyvisa.ResourceManager()
    rm.list_resources()

    try:
        inst = rm.open_resource(rm.list_resources()[0])
        power_meter = ThorlabsPM100.ThorlabsPM100(inst=inst)

        #Unit by default :
        Unit=" W"

        #Creating window
        root = tk.Tk()
        frm = ttk.Frame(root, padding=10)
        root.iconbitmap("C:/Users/manip/Desktop/Ian (Alternant)/fresnel.ico")
        frm.grid()
        root.geometry("500x300")
        root.title("PM100 Python GUI")

        #Measurement
        Label(frm, text="Measurement Type :").grid(column=0, row=0)
        TypePower=Button(frm, text="Power",command=ConfigurePower).grid(column=0, row=1)
        TypeCurrent=Button(frm, text="Current",command=ConfigureCurrent).grid(column=1, row=1)

        Display=Label(frm, text=str(power_meter.read)+Unit)
        Display.grid(column=0, row=2)

        #Wavelength
        Label(frm, text="Wavelength (400-1100 nm):").grid(column=0, row=3)
        global entryLambda
        entryLambda = tk.Entry(root)
        entryLambda.grid(column=2, row=3, sticky="nesw")
        entryLambda.insert(0,"561")
        power_meter.sense.correction.wavelength = 561
        ButtonLambda=Button(frm,text="Change Lambda", command=ConfigureLambda)
        ButtonLambda.grid(column=0, row=4)

        #Frequency ?


        root.mainloop()

    except IndexError:
        print("Error : No power meter detected")