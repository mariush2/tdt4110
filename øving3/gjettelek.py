# This Python file uses the following encoding: utf-8
import os, sys, random


def gjettelek(hoyest):
    tilfeldig_tall = random.randint(1, hoyest)
    gjettet = False

    while (not(gjettet)):
        try:
            input_gjettet = int(input("Gjett ett tall: "))

            if (input_gjettet == tilfeldig_tall):
                print("Du gjettet riktig!")
                gjettet = True

            elif (input_gjettet > tilfeldig_tall):
                print("Det rettet tallet er lavere!")

            else:
                print("Det rettet tallet er høyere!")


        except ValueError:
            print("Du skrev ikke inn et tall!")


def get_values():
    try:
        hoyest = int(input("Skriv inn den øvre grensen: "))
        gjettelek(hoyest)

    except ValueError:
        print("Du skrev ikke inn et tall, prøv igjen!")
        get_values()


get_values()
