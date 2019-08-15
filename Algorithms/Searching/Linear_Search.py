def search(a, n, y):
    for i in range(0, n):
        if a[i] == y:
            return i
    return -1


n = int(input("Enter the number of elements in array : "))
a = []
print("Enter the elements : \n")
for j in range(n):
    x = int(input())
    a.append(x)
y = int(input("Enter the element to be searched : "))
n = len(a)
result = search(a, n, y)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)