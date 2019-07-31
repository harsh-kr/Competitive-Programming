def insertion_sort(a):
    # Traverse through 1 to len(arr)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    print(a)


lst = []
size = int(input("Enter size of the list: \t"))

for i in range(size):
    elements = int(input("Enter the element: \t"))
    lst.append(elements)

insertion_sort(lst)