def quicksort(list1, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(list1, start, end)
        quicksort(list1, start, p)
        quicksort(list1, p + 1, end)


def partition(list1, start, end):
    pivot = list1[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and list1[i] <= pivot:
            i = i + 1
        while i <= j and list1[j] >= pivot:
            j = j - 1

        if i <= j:
            list1[i], list1[j] = list1[j], list1[i]
        else:
            list1[start], list1[j] = list1[j], list1[start]
            return j


list1 = input('Enter the list of numbers: ').split()
list1 = [int(x) for x in list1]
quicksort(list1, 0, len(list1))
print('Sorted list: ', end='')
print(list1)
