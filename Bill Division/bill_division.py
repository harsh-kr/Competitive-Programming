def bonAppetit(bill, k, b):
    sum = 0
    for i in range(len(bill)):
        if i == k:
            pass
        else:
            sum = sum+bill[i]
    bactual = int(sum/2)
    if bactual == b:
        print("Bon Appetit")
    else:
        print(b-bactual)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)