def findnumberofTriangles(arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(0, n - 2):
        k = i + 2
        for j in range(i + 1, n):
            while k < n and arr[i] + arr[j] > arr[k] :
                k += 1
            if k > j:
                count += k - j - 1
    return count


arr = [10, 21, 22, 100, 101, 200, 300]
print("Number of Triangles:", findnumberofTriangles(arr))