def reVal(num):

    if (num >= 0 and num <= 9):
        return chr(num + ord('0'))
    else:
        return chr(num - 10 + ord('A'))


def fromDeci(res, base, inputNum):
    while (inputNum > 0):
        res += reVal(inputNum % base)
        inputNum = int(inputNum / base)

    return res[::-1]


inputNum = 282
base = 16
res = ""
print(fromDeci(res, base, inputNum))
