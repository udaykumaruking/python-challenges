def realtiveSpeed(dir, d1, d2, s1, s2):
    time1 = d1 / s1
    time2 = d2 / s2
    if dir == 0:
        return (int(abs(time1 + time2)))
    else:
        return (time1 - time2)


dir = int(input("dir: "))
d1 = int(input('d1: '))
d2 = int(input('d2: '))
s1 = int(input('s1: '))
s2 = int(input('s2: '))

print(realtiveSpeed(dir, d1, d2, s1, s2))
