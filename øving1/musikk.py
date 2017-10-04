# This Python file uses the following encoding: utf-8
import os, sys

antall_input = input("Hvor mange 10-toners melodilinjer tror du at du har hørt? ")

def sjekk_melodier():
    total = 8.25e19
    hort = antall / total
    print("Du har hørt", hort, "prosent av mulige melodilinjer")


try:
    antall = float(antall_input)
    sjekk_melodier()
except ValueError:
    print("Du skrev ikke inn et tall!")
