# This Python file uses the following encoding: utf-8
import os, sys, math

#Oppgave a
def sum(r, n):
    print("""
---------------------------------------------------
 _____
|  _  |
| | | |_ __  _ __   __ _  __ ___   _____      __ _
| | | | '_ \| '_ \ / _` |/ _` \ \ / / _ \    / _` |
\ \_/ / |_) | |_) | (_| | (_| |\ V /  __/   | (_| |
 \___/| .__/| .__/ \__, |\__,_| \_/ \___|    \__,_|
      | |   | |     __/ |
      |_|   |_|    |___/

    """)

    sum = 0
    while(n >= 0):
        sum += r ** n
        n -= 1

    print("Summen av rekken er", sum)
    print("---------------------------------------------------")

#Oppgave b og c
def uendelig_sum(r, tol):
    print("""
----------------------------------------------------------------------
 _____                                       _
|  _  |                                     | |
| | | |_ __  _ __   __ _  __ ___   _____    | |__         ___
| | | | '_ \| '_ \ / _` |/ _` \ \ / / _ \   | '_ \       / __|
\ \_/ / |_) | |_) | (_| | (_| |\ V /  __/   | |_) |  _  | (__
 \___/| .__/| .__/ \__, |\__,_| \_/ \___|   |_.__/  ( )  \___|
      | |   | |     __/ |                           |/
      |_|   |_|    |___/

    """)
    sum = 0
    final = 2
    antall = 0

    while( not(math.isclose(final, sum, abs_tol=tol)) ):
        sum = (1 - r ** (antall + 1)) / (1 - r)
        antall += 1

    print("For å være innenfor toleransegrensen:", tol, ", kjørte løkken", antall, "ganger.")
    print("Differansen mellom den virkelige og estimerte verdien var da", abs(final - sum))
    print("----------------------------------------------------------------------")


def get_values():
    try:
        r = float(input("Skriv inn 'r': "))
        n = int(input("Skriv inn 'n': "))
        tol = float(input("Skriv inn toleransegrensen (f.eks. 0.01): "))

        if((1 <= tol <= 0) or (-1 > r > 1)):
            raise ValueError

        sum(r, n)
        uendelig_sum(r, tol)
    except ValueError:
        print("Du skrev inn noe feil, prøv igjen!")
        get_values()


get_values()
