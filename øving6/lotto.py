import random
numbers = []
vunnet = 0
brukt = 0

def main():
    global numbers
    for i in range(1, 35):
        numbers.append(i)

    guessed = get_guesses()
    lotto_nums = draw_num(7)
    add_nums = draw_num(3)

    amount_lotto = compList(guessed, lotto_nums)
    amount_add = compList(guessed, add_nums)

    amount_won = str(won(amount_lotto, amount_add))
    print("Lotto:", amount_lotto)
    print("Add:", amount_add)
    print("Du vant " +  amount_won + "!")


def get_guesses():
    myGuess = []
    try:
        for number in input("Skriv inn tallene du gjetter (separer med mellomrom): ").split():
            myGuess.append(int(number))

        for i in myGuess:
            if(myGuess.count(i) != 1 or i > 34 or i < 1):
                raise ValueError

        if(len(myGuess) != 7):
            raise ValueError

        return myGuess

    except ValueError:
        print("Du skrev inn noe feil, prøv igjen!")
        return get_guesses()


def draw_num(n):
    global numbers
    new_list = []

    if(len(numbers) < n):
        print("Ran out of numbers to draw!")
        exit()

    for i in range(0, n):
        new_random = random.randint(0, len(numbers) - 1)
        new_list.append(numbers[new_random])
        numbers.pop(new_random)

    return new_list


def compList(list1, list2):
    amount = 0
    for index, i in enumerate(list1):
        for j in list2:
            if(i == j):
                amount += 1

    return amount


def won(lotto, add):
    prize = [2749455, 102110, 3385, 95, 45]

    if(lotto == 7):
        return prize[0]
    elif(lotto == 6 and add == 1):
        return prize[1]
    elif(lotto == 6):
        return prize[2]
    elif(lotto == 5):
        return prize[3]
    elif(lotto == 4 and add == 1):
        return prize[4]
    else:
        return 0

#Siste del
def random_guess():
    guessList = []
    for i in range(1, 35):
        guessList.append(i)

    myGuess = []
    for i in range(0, 7):
        index = random.randint(0, len(guessList) - 1)
        myGuess.append(guessList[index])
        guessList.pop(index)

    return myGuess


def random_main():
    global numbers, vunnet, brukt

    plays = 1000000
    for i in range(0, plays):
        numbers = []
        for j in range(1, 35):
            numbers.append(j)

        guessed = random_guess()
        lotto_nums = draw_num(7)
        add_nums = draw_num(3)

        amount_lotto = compList(guessed, lotto_nums)
        amount_add = compList(guessed, add_nums)

        amount_won = won(amount_lotto, amount_add)
        print("Du vant " +  str(amount_won) + "!")
        vunnet += amount_won
        brukt += 5

    print("Du vant:", str(vunnet), "på", str(plays), "forsøk.")
    print("Du brukte:", str(brukt))
    print("Du tjente altså", str(vunnet - brukt))

random_main()
