# This Python file uses the following encoding: utf-8
import os, sys

skatt_prosent = 0.5

type_bolig = input("Skriv inn type bolig (egen bolig/sekundærbolig/fritidsbolig) du har leid ut: ")

#Oppgave a
def egen_bolig():
    print("""---------------------------------------------------------------------\n
     _____                   _           _ _
    |  ___|                 | |         | (_)
    | |__  __ _  ___ _ __   | |__   ___ | |_  __ _
    |  __|/ _` |/ _ \ '_ \  | '_ \ / _ \| | |/ _` |
    | |__| (_| |  __/ | | | | |_) | (_) | | | (_| |
    \____/\__, |\___|_| |_| |_.__/ \___/|_|_|\__, |
           __/ |                              __/ |
          |___/                              |___/

    Dette programmet besvarer om din utleie av egen bolig er skattepliktig.
    Først trenger vi å vite hvor stor del av egen bolig du har leid ut.
    Angi dette i prosent, 100 betyr hele boligen, 50 betyr halve,
    20 en mindre del av boligen som f.eks. en hybel.
    \n----------------------------------------------------------------------\n""")

    #global skatt_prosent

    bolig_leid_ut = input("Oppgi hvor mye av boligen som blir leid ut (i prosent): ")
    leieinntekt = input("Skriv inn årlig leieinntekt: ")

    print('\n---------------------------------------------------------------------\n')

    try:
        bolig_leid_ut = float(bolig_leid_ut)
        leieinntekt = float(leieinntekt)

        if(bolig_leid_ut > 50 or leieinntekt < 20000):
            skatt = int(leieinntekt * skatt_prosent)

            print("Inntekten er skattepliktig")
            print("Totalt skattepliktig beløp er", skatt)
        else:
            print("Inntekten er ikke skattepliktig.")
    except ValueError:
        print("Du skrev inn noe feil!")
        egen_bolig()



#Oppgave b
def annen_bolig():
    print("""---------------------------------------------------------------------\n
    Dette programmet besvarer om din utleie en annen type bolig,
    her sekundær- eller fritidsbolig, er skattepliktig.
    Først trenger vi å vite om du leier ut en sekundær- eller en fritidsbolig.
    \n---------------------------------------------------------------------\n""")

    global type_bolig
    global skatt_prosent

    print('Du har valgt %s.' % (type_bolig))
    print('Nå trenger vi først å vite om %sen(e) primært brukes til utleie eller fritid.' % (type_bolig))
    print('Deretter trenger vi å vite hvor mange %ser du leier ut.' % (type_bolig))
    print('Til slutt trenger vi å vite hvor store utleieinntekter du har per %s' % (type_bolig))
    print('\n---------------------------------------------------------------------\n')

    bolig_formaal = input("Skriv inn formålet med %s(e) (fritid/utleie): " % (type_bolig))
    bolig_antall = input("Skriv inn antallet fritidsboliger du leier ut: ")
    utleieinntekt_per = input("Skriv inn utleieinntekten pr. fritidsbolig: ")

    print('\n---------------------------------------------------------------------\n')

    try:
        bolig_formaal = bolig_formaal.lower()
        bolig_antall = int(bolig_antall)
        utleieinntekt_per = float(utleieinntekt_per)

        if((bolig_formaal == "utleie" or bolig_formaal == "fritid") and bolig_antall > 0 and utleieinntekt_per > 0):
            #Gikk igjennom testen, og sjekket at alle verdiene er lovlige
            skattepliktig = False

            #Beregning
            if(type_bolig == "sekundærbolig" or bolig_formaal == "utleie"):
                #Hvis type_bolig ikke er sekundær, er den fritid, derfor blir alle sekundærboligene tatt fordi
                #if setningen starter med denne...
                skattepliktig = True
                skatt_per = utleieinntekt_per * skatt_prosent
                total_skatt = skatt_per * bolig_antall

            elif(utleieinntekt_per > 10000):
                #85% skattepliktig
                skattepliktig = True
                overskytende_per = utleieinntekt_per - 10000
                skatt_per = overskytende_per * 0.85 #85% skatt hvis fritidsbolig, brukt til fritid, og mer enn 10k inntekt
                total_skatt = skatt_per * bolig_antall #Skatt per * antall

            #Utprinting
            if(skattepliktig): #Hvis skattepliktig, start printing av verdiene

                print("Inntekten er skattepliktig")

                try:
                    #Gjør dette bare om overskytende_per er definert
                    overskytende_per = int(overskytende_per)
                    print("Overskytende beløp per", type_bolig, "er",overskytende_per)

                except NameError:
                    print("Skattepliktig inntekt per", type_bolig, "er", skatt_per)
                    print("Totalt skattepliktig beløp er", total_skatt)

            else:
                print("Inntekten er ikke skattepliktig.")

        else:
            raise ValueError
    except ValueError:
            print("Du skrev inn noe feil!")
            annen_bolig()


try:
    type_bolig = type_bolig.lower()
    if(type_bolig == "fritidsbolig" or type_bolig == "sekundærbolig"):
        #Sjekker om brukeren har skrevet inn riktig
        annen_bolig()
    elif(type_bolig == "egen bolig"):
        egen_bolig()
    else:
        raise ValueError
except ValueError:
    print("Du skrev inn noe feil!")
