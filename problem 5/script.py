def SumNumbersDivisible(a, b):
    ans = 0
    for i in range(m, n+1):
        if i % 5 == 0:
            if i % 3 == 0:
                ans += i
    return ans


m = int(input("Enter First Integer value: "))
n = int(input("Enter First Integer value: "))
print(SumNumbersDivisible(m, n))
