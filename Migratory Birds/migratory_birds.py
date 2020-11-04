from collections import Counter
def migratoryBirds(arr):
    c = Counter(arr)
    max_birds = max(c.values())
    return min([x for x in c if c[x] == max_birds])


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)