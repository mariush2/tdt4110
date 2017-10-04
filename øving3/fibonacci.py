# This Python file uses the following encoding: utf-8
import os, sys

fib_seq = [1, 1]


def fibonacci(k, left):
    global fib_seq
    end = len(fib_seq) - 1

    if(left > 2):
        new_value = fib_seq[end - 1] + fib_seq[end]
        fib_seq.append(new_value)

        left -= 1
        fibonacci(k, left)
    else:
        onsket_tall = fib_seq[end]
        sum = 0

        if(k == 1 or k == 2):
            sum = k
        else:
            for x in fib_seq:
                sum += x

        print("--------------------------------------------")
        print("Det ", k,". tallet i fibonacci sekvensen er '", onsket_tall, "'", sep='') #sep='' bestemmer seperation av variablene
        print("Summen av de", k, "første tallene er", sum)
        print("Liste opp til og med f(k):", fib_seq)
        print("--------------------------------------------")
        print("")



def get_values():
    try:
        k = int(input("Skriv inn k: "))
        left = k
        print("")
        fibonacci(k, left)
    except ValueError:
        print("Du skrev inn noe feil, prøv på ny!")
        get_values()


get_values()
