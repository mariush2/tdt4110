def gcd(a, b):
    while (b != 0):
        gammel_b = b
        b = a % b
        a = gammel_b
    return a


def reduce_fraction():
    a = input("Skriv inn et heltall 'a': ")
    b = input("Skriv inn et heltall 'b': ")
    try:
        a = int(a)
        b = int(b)
        d = int(gcd(a,b))

        new_a = int(a / d)
        new_b = int(b / d)

        ans = str(new_a) + " / " + str(new_b)
        return ans

    except ValueError:
        print("Du skrev inn noe feil, prøv igjen.")
        reduce_fraction()

print(reduce_fraction())
