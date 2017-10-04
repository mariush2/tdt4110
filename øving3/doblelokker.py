# This Python file uses the following encoding: utf-8
import os, sys, math

def lille_gangetabellen():

    for faktor in range(1,10):
        print(faktor, "-gangen",sep='')
        for tall in range(1,11):
            print(faktor * tall)


def finn_primtall():

    print("Primtall mellom 0 og 100")
    primtall = []
    for n in range(2, int(10e8)):
        if(not(n in primtall)):
            if((n % 2 != 0 and n > 2)):
                #fjerner alle partall ettersom de er delelige på 2 (bortsett ifra 2)
                er_primtall = True
                for i in range(3, int(math.sqrt(n)) + 1, 2):
                    #Range starter på 3 fordi vi trenger ikke sjekke om deleling på 1 og 2.
                    #Opp til n^2 + 1 fordi når man treffer n^2 er det delelig på seg selv
                    #Step = 2 fordi vi trenger ikke sjekke partall, ettersom bare oddetall > 2, er primtall
                    if(n % i == 0 and n != i):
                        #Ikke primtall
                        er_primtall = False


                if(er_primtall):
                    #Legger primtallet som er funnet i listen "primtall"
                    #print("Legger til", n, "fordi det er et primtall")
                    primtall.append(n)

    print(primtall)


#finn_primtall()
lille_gangetabellen()
