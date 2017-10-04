antall_kvinner, antall_menn, antall_fag, antall_ITGK, antall_timer_lekser = 0, 0, 0, 0, 0
medlem_ITGK = False
alder = 0

def main():
    global antall_kvinner, antall_menn

    print("-"*80 + "\n" + " "*23 + "-Den Store Spørreundersøkelsen-\n")
    print(" "*4 + "Husk at du kan skrive 'hade' når som helst for å avslutte undersøkelsen")
    print("-"*80 + "\n")

    while True:
        #Lagrer de forrige verdiene, i tilfelle at personen er utenfor målgruppen
        #må vi tilbakestille verdiene til det de var før
        old_antall_menn = antall_menn
        old_antall_kvinner = antall_kvinner
        #Sjekk kjønn
        sjekk_kjonn()
        if(sjekk_alder()):
            #innenfor ønsket gruppe
            if(sjekk_fag()):
                #Sjekk om personen har ITGK
                sjekk_itgk()

                #Sjekk antall timer
                sjekk_timer()

        else:
            antall_menn = old_antall_menn
            antall_kvinner = old_antall_kvinner


        print("\n\n" + "-"*20)
        print("Antall menn:", antall_menn)
        print("Antal kvinner:", antall_kvinner)
        print("Antall fag:", antall_fag)
        print("ITGK medlem:", medlem_ITGK)
        print("Antall ITGK:", antall_ITGK)
        print("Antall timer lekser:", antall_timer_lekser)
        print("-"*20 + "\n\n")


def sjekk_hade(svar):
    svar.lower()

    if(svar == "hade"):
        print("Takk for at du bidro :-)")
        exit()


def sjekk_kjonn():
    global antall_menn, antall_kvinner

    kjonn = input("Skriv inn kjønn(m/f): ")
    kjonn = kjonn.lower()
    sjekk_hade(kjonn)

    if(kjonn == "m"):
        antall_menn += 1
    elif(kjonn == "f"):
        antall_kvinner += 1
    else:
        print("Du skrev inn noe feil, prøv igjen. (Husk å bruk 'm' eller 'f' for å velge kjønn!)")
        sjekk_kjonn()


def sjekk_alder():
    global alder
    alder = input("Skriv inn alder: ")
    sjekk_hade(alder)
    try:
        alder = int(alder)
        if(alder > 0):
            if(not(alder >= 16 and alder <= 25)):
                #Fortsett undersøkelsen
                print("Du er ikke innenfor ønsket målgruppe for undersøkelsen")
                return False
            else:
                return True
        else:
            print("Du skrev inn et negativt tall! Prøv igjen")
            sjekk_alder()

    except ValueError:
        print("Du skrev inn noe feil! Prøv igjen")
        sjekk_alder()


def sjekk_fag():
    global antall_fag

    fag = input("Tar du et fag(j/n)? ")
    fag = fag.lower()
    sjekk_hade(fag)

    if(fag == "j"):
        antall_fag += 1
        return True
    elif(fag == "n"):
        print("Takk for at du bidro!")
        return False
    else:
        print("Du skrev inn noe feil, prøv igjen. (Husk å bruke 'j' eller 'n' for å svare!)")
        sjekk_fag()


def sjekk_itgk():
    global antall_ITGK, medlem_ITGK, alder

    if(alder < 22):
        itgk = input("Tar du ITGK(j/n)? ")
    else:
        itgk = input("Tar virkelig du ITGK(j/n)? ")

    itgk = itgk.lower()
    sjekk_hade(itgk)

    if(itgk == "j"):
        medlem_ITGK = True
        antall_ITGK += 1
    elif(itgk == "n"):
        medlem_ITGK = False
    else:
        print("Du skrev inn noe feil, prøv igjen. (Husk å bruke 'j' eller 'n' for å svare!)")
        sjekk_itgk(itgk)


def sjekk_timer():
    global antall_timer_lekser

    timer_input = input("Hvor mange timer bruker du daglig på lekser? ")
    sjekk_hade(timer_input)

    try:
        timer_input = int(timer_input)
        if(timer_input < 0):
            raise ValueError

        antall_timer_lekser += timer_input

    except ValueError:
        print("Du skrev ikke inn en gyldig verdi! Prøv igjen")
        sjekk_timer()

main()
