upto = int(input("How many integers do you want to show: "))
# Initialzation
f0 = 0  # int
f1 = 1  # int
output = []  # list
output.append(f0)
output.append(f1)

for i in range(upto-2):
    temp = f0 + f1
    (f0, f1) = (f1, temp)
    output.append(temp)
print(output)
