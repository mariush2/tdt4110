# This Python file uses the following encoding: utf-8
import os, sys

antall_dager = input("Dager til du skal reise? ")

pris = 0


def regn_ut_pris():
    global pris

    if antall_dager < 14:
        pris = 199
        print("Vi tilbyr minipris: %d,- kan ikke refunderes/endres" % (pris))
        tilbud()

    else:
        pris = 440
        alders_rabatt()



def tilbud():
    global pris

    svar = input("Ønskes dette (J/N)? ") #input() funket ikke?
    svar = svar.upper()


    if (svar == "J"):
        print("Takk for pengene, god reise!")

    elif (svar == "N"):
        pris = 440
        alders_rabatt()

    else:
        print("Svar ja ved å skrive inn 'J' og nei ved å skrive inn 'N'")
        tilbud()


def alders_rabatt():
    global pris

    #Spør brukeren om alder, redirect til annen_rabatt om
    alder = input("Skriv inn din alder: ")

    try:
        alder = int(alder)
    except ValueError:
        print("Skriv inn alderen på ny!")
        alders_rabatt()


    if (alder < 16):
        #50% rabatt
        pris = pris * 0.5

    elif (alder > 60):
        #25% rabatt
        pris = pris * 0.75

    else:
        annen_rabatt()


def annen_rabatt():
    global pris

    #Spør brukeren om student eller militær personell
    svar = input("Er du student eller militær (J/N)? ")
    svar = svar.upper()

    if (svar == "J"):
        #25% rabatt
        pris = pris * 0.75

    elif (svar == "N"):
        #prisen blir uendret
        pris = pris

    else:
        print("Svar ja ved å skrive inn 'J' og nei ved å skrive inn 'N'")
        annen_rabatt()


try:
    antall_dager = int(antall_dager)
    regn_ut_pris()
    print("Totalen ble: %d,-" % (pris))
except ValueError:
    print("Du skrev ikke inn et tall!\nHusk at du bare kan skrive inn hele tall.")
