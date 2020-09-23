def reVal(abc):
    if (abc >= 0 and abc <= 9):
        return abc
    else:
        return chr(abc - 10 + ord('A'))


def fromDeci(res, n, num):
    # index = 0
    while (num > 0):
        qu, re = divmod(num, n)
        res += str(reVal(qu))
        num = int(re)
    return res[::-1]


n = 12
num = 718
res = ''
print(fromDeci(res, n, num))
