import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap = []
    counta = 0
    ora = []
    counto = 0
    for i in apples:
        i += a
        ap.append(i)
    for j in oranges:
        j += b
        ora.append(j)
    for k in ap:
        if s <= k <= t:
            counta += 1
    for l in ora:
        if s <= l <= t:
            counto += 1
    print(counta)
    print(counto)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
