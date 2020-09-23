# Cumulative Discount
# Discounted Price = Marked Price * (100 - discount%) / 100
# Discount% = 100 - (Discounted Price * 100 / Marked Price)

def discountPer(val, out, size):
    mp = 100
    for j in range(leng):
        mp = mp * (100 - float(val[j]))/100

    return 100 - (mp * 100 / 100)
    # return mp


#markedPrice = 100
arr = input()
n = int(input())
arr = list(arr.split(" "))
# length = len(arr)
# print(length)
op = 0
leng = len(arr)
for i in range(leng):
    op = discountPer(list(arr), float(op), int(n))
print(op)
