import os


def birthday(s, d, m):
    count = 0
    for i in range(len(s)-m+1):
        sum = 0
        for j in range(i,i+m):
            sum = sum+s[j]
        if sum == d:
            count += 1
    return count


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)