import numpy as np

def allUnique(lst):
    return len(lst) == len(set(lst))


def removeDuplicates(lst):
    return list(set(lst))


def inAbutnotB(a, b):
    return [x for x in set(a) if x not in set(b)]


# print(allUnique([1,3,2,5]))
# print(allUnique([1,2,3,1,1,]))
# print(removeDuplicates([1,3,5,2,1,1,3,]))
# print(inAbutnotB([1,2,3, 6, 99, 10, 14], [2,5,6,1]))

# Ekstra oppgave
def areOthogonal(a,b):
    new = np.array([a, b])
    sum = 0
    end = len(a)
    for x in range(0, len(a)):
        sum += new[0][x] * new[1][x]

    if(sum == 0):
        print("a = " + str(a) + " er otrogonal med b = " + str(b))
        return True
    else:
        print("Vektorene er ikke ortogonale")
        return False

#Ikke otrogonal
#print(areOthogonal([1,2,3], [3,2,6]))

#Ortogonal
#print(areOthogonal([1,-1,0], [2,2,3]))

array = np.arange(1,16)
new_array = np.transpose(array).reshape((5,3), order="F")
print(array)
print(new_array)
