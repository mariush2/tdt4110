from math import *

def recursive_sum(n):
    if(n == 1):
        return 1
    else:
        return n + recursive_sum(n-1)


def find_smallest_element(numbers, current_min = None):
    if(not numbers):
        return current_min
    #Removes and selects the last item in the list
    candid = numbers.pop()
    if(current_min == None or candid < current_min):
        return find_smallest_element(numbers, candid)
    return find_smallest_element(numbers, current_min)


def binary_search(numbers, element):
    if(numbers[-1] < element or numbers[0] > element):
        return -float("inf")

    if(len(numbers) % 2 != 0):
        m = int(len(numbers)-1)/2
    else:
        m = int(len(numbers)/2) - 1

    if(numbers[m] < element):
        return binary_search(numbers[m+1:], element) + int(len(numbers[0:m+1]))
    elif(numbers[m] > element):
        return binary_search(numbers[:m], element)
    else:
        return m



#recursive_sum(3)
#find_smallest_element([2,3,5,6,1,2,3,5])

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
binary_search(numbers, 10)
