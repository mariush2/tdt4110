# This Python file uses the following encoding: utf-8
import os, sys
import math


hoyde_input = input('Skriv inn høyden for tetraederet: ')

def areal_func():
    areal = math.sqrt(3) * a ** 2
    areal = round(areal, 3)
    print("Overflatearealet ble: ",areal)


def volum_func():
    volum = (math.sqrt(2) * a ** 3) / (12)
    volum = round(volum, 3)
    print("Arealet ble: ",volum)


try:
    hoyde = float(hoyde_input)
    a = (3/math.sqrt(6)) * hoyde

    print("Høyden du satte inn:",hoyde)

    areal_func()
    volum_func()
except ValueError:
    print("Du skrev ikke inn et tall!")
