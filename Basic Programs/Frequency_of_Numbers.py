arr = []
n = int(input("Enter the length of array : "))
for i in range(n):
    no = int(input("Enter the number : "))
    arr.append(no)

# Array temp will store frequencies of element
temp = [None] * n
visited = -1

for i in range(0, n):
    count = 1
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            count = count + 1
            # To avoid counting same element again
            temp[j] = visited

    if (temp[i] != visited):
        temp[i] = count

# Displays the frequency of each element present in array
print("---------------------")
print(" Element | Frequency")
print("---------------------")
for i in range(0, len(temp)):
    if (temp[i] != visited):
        print("    " + str(arr[i]) + "    |    " + str(temp[i]))
print("---------------------")