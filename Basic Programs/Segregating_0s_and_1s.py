def segregate0and1(arr, size):
    zero = 0
    one = size - 1

    while zero < one:
        if arr[zero] == 1:
            (arr[zero],arr[one]) = (arr[one], arr[zero])
            one -= 1
        else:
            zero += 1


# Driver Code
arr = [0, 1, 0, 1, 1, 1]
arr_size = len(arr)
segregate0and1(arr, arr_size)
print("Array after segregation is", end=" ")
for i in range(0, arr_size):
    print(arr[i], end=" ")