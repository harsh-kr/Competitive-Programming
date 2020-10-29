def birthdayCakeCandles(ar):
    maximum = 0
    count = 0
    for i in ar:
        if i > maximum:
            maximum = i
    for j in ar:
        if j == maximum:
            count += 1
    return count


if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print(result)
