def primeChecker(n):
    if n < 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True
    n1 = int(n * 0.5)
    f = 5
    while f <= n1:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


val = int(input("Enter any Number: "))
printer = bool(primeChecker(val))
print(printer)
