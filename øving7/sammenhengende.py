import random

def randList(size, lower, upper):
    list = []
    for i in range(0, size):
        list.append(random.randint(lower, upper))
    return list


def compareLists(list1, list2):
    bigger = len(list1) > len(list2)
    while len(list1) != len(list2):
        if(bigger):
            #Must extend list2
            list2.append(None)
        else:
            #Must extend list1
            list1.append(None)

    unique = []
    for num in list1:
        #We now know that the lists are the same length
        if num in list1 and num in list2:
            unique.append(num)


    return removeDuplicates(unique)


def removeDuplicates(lst):
    return list(set(lst))


def multiCompLists(lists):
    unique = []

    for list in lists:
        for num in list:
            inAll = True
            for i in range(0, len(lists)):
                if not(num in lists[i]):
                    inAll = False
            if(inAll):
                unique.append(num)

    return removeDuplicates(unique)


def longestEven(list):
    even = True
    even_nums = []
    for i in range(0, len(list)):
        if(list[i] % 2 == 0):
            #Tallet er et partall
            even_nums.append(True)
        else:
            even_nums.append(False)

    even_amount = 0
    start_index = -1
    biggest = 0
    for index, even in enumerate(even_nums):
        if(even):
            even_amount += 1
            if(even_amount > biggest):
                #Så er det den største strengen med partall
                start_index = index - biggest
                biggest = even_amount
        else:
            even_amount = 0

    return biggest, start_index


def main():
    print(randList(10,2,7))
    a = [1,2,3]
    b = [4,3,1]
    print(compareLists(a,b))
    c = [7,2,1]
    d = [a,b,c]
    print(multiCompLists(d))
    list = [4,3,3,6,2,6,8,3,4,3,3]
    print(longestEven(list))

main()
