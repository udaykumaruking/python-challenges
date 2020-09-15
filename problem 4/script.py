import math as pr
string = input()
beforeList = (string.split(', '))
# print(type(beforeList))

# print("..........")
# print(beforeList)
# print("..............")
# 1, 2, 3, 4, 51, 2, 3, 4, 5print(mul)
afterList = list(map(int, beforeList))

mul = pr.prod(afterList)
