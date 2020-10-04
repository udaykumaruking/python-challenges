parti = int(5)
lis = '-7 -7 -7 -7 -6'
lis = set(lis.split(" "))
#sorted(scoresList)
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))
print (max(lis))