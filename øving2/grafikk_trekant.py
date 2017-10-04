from turtle import *
# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")
spiss = input("Ønsker du spissen på trekanten opp eller ned (O / N)? ")
pen_farge = input("Velg pennefarge, NTNU-rosa (R) eller NTNU-oransj (O): ")
fill_farge = input("Velg fillfarge, NTNU-gul (G), NTNU-lyseblå (LB) eller brun (B): ")


def tegn_trekant():
    pensize(7)
    if(pen_farge == "o"):
        pencolor("#f58025")
    else:
        pencolor("#ad208e")

    bgcolor("#00509e")     # sett bakgrunnsfargen blå

    if(fill_farge == "g"):
        fillcolor("#f1d282") # sett fyllfargen gul
    elif(fill_farge == "b"):
        fillcolor("#90492d") # sett fyllfargen brun
    else:
        fillcolor("#5cbec9")

    begin_fill()
    forward(200)

    if(spiss == "o"):
        left(120)
        forward(200)
        left(120)
    else:
        right(120)
        forward(200)
        right(120)

    forward(200)
    end_fill()
    penup()
    goto(-100, 200)
    fillcolor("#ffffff")
    pencolor("#ffffff")
    write("Trykk på skjermen for å avslutte.", font=("Arial", 20, "normal"))
    exitonclick()


try:
    spiss = spiss.lower()
    pen_farge = pen_farge.lower()
    fill_farge = fill_farge.lower()

    fill_correct = fill_farge == "g" or fill_farge == "lb" or fill_farge == "b"
    pen_correct = pen_farge == "r" or pen_farge == "o"
    spiss_correct = spiss == "o" or spiss == "n"

    if(not(fill_correct and pen_correct and spiss_correct)):
        raise ValueError
    tegn_trekant()
except ValueError:
    print("Du skrev inn noe feil!")
