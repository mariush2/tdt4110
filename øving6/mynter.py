def count_coins(coins):
    return sum([i for i in coins])


def num_coins(numbers):
    needed = []
    for i in numbers:
        current_needed = [0, 0, 0, 0]
        while i > 0:
            if(i % 20 == 0):
                current_needed[0] += 1
                i -= 20
            elif(i % 10 == 0):
                current_needed[1] += 1
                i -= 10
            elif(i % 5 == 0):
                current_needed[2] += 1
                i -= 5
            else:
                current_needed[3] += 1
                i -= 1

        needed.append(current_needed)

    return needed


def check_weight(numbers):
    weight = 0
    weight_list = [9.9, 6.8, 7.85, 4.35]
    needed = num_coins(numbers)
    print(needed)

    for list in needed:
        for index, i in enumerate(list):
            weight += i*weight_list[index]

    return weight

#print(check_weight([20, 10]))
count_coins([20, 15, 10])
