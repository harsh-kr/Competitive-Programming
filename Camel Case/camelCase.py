def camelcase(s):
    count = 1
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            count += 1
    return count


if __name__ == '__main__':

    s = input()

    result = camelcase(s)

    print(result)
