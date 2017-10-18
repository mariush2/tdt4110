def bubble_sort(list):
    sorted = False
    while not(sorted):
        sorted = True
        for i in range(0, len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                sorted = False

    return list


def selection_sort(list):
    sorted_list = []
    sorted = False
    while not(sorted):
        biggest = 0
        sorted = True
        for i in range(0, len(list)):
            if list[biggest] < list[i]:
                biggest = i
                sorted = False

        if(sorted):
            for i in list:
                sorted_list.append(i)
        else:
            sorted_list.append(list.pop(biggest))

    return sorted_list


print(bubble_sort([1,7,6,18,6,3,1,0,3,7,59]))
print(selection_sort([1,7,6,18,6,3,1,0,3,7,59]))
