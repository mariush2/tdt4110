# This Python file uses the following encoding: utf-8
import os, sys


def clear():
    os.system('clear')


def game(hemmelig_ord, antall_liv):
    gjettet_ord = []
    for x in hemmelig_ord:
        gjettet_ord.append("_")

    while True:
        gjettet_bokstav = input("Gjett en bokstav: ")
        feil = 0;

        if(len(gjettet_bokstav) > 1):
            print("Du kan bare gjette en bokstav om gangen!")

        elif(not(gjettet_bokstav in gjettet_ord)): #Hvis brukeren ikke skriven inn det samme som tidligere
            for i in range(len(hemmelig_ord)):
                if(gjettet_bokstav == hemmelig_ord[i]):
                    #Brukeren gjettet riktig
                    gjettet_ord[i] = hemmelig_ord[i]
                    feil += 1
                else:
                    #Trekkes 1 gang per bokstav, if-setningen nedenfor fikser dette slik at spilleren bare mister 1 liv per runde.
                    feil -= 1


            if (feil <= -len(hemmelig_ord)):
                antall_liv -= 1
                print("Du gjettet feil!")

            elif(feil > -len(hemmelig_ord)):
                print("Du gjettet riktig!")


            if(antall_liv == 0):
                print("Du tapte!")
                break

            elif(gjettet_ord == hemmelig_ord):
                print("Gratulerer! Du vant!")
                print("Ordet du gjettet riktig var '", "".join(hemmelig_ord), "'", sep="")
                break

            else:
                print("Dette er ordet til nå:", " ".join(gjettet_ord))
                print("Du har", antall_liv, "liv igjen.")

        else:
            print("Du har allerede gjettet den bokstaven!")

        print("\n")

def get_values():
    try:
        hemmelig_input = input("Skriv inn det hemmelige ordet: ")
        antall_liv = int(input("Skriv inn antall liv: "))

        if(antall_liv <= 0):
            raise ValueError

        hemmelig_ord = []
        for bokstav in hemmelig_input:
            hemmelig_ord.append(bokstav)

        clear()
        game(hemmelig_ord, antall_liv)
    except ValueError:
        print("Du skrev inn noe feil, prøv på ny!")
        get_values()


get_values()
