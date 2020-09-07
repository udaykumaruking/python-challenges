import string


def pangramChecker(str):
    str = str.lower()
    strSet = set(str)
    #alpha = 'abcdefghijklmnopqrstuvwxyz'
    punSet = set(string.punctuation)
    finSet = strSet - punSet

    if len(finSet) != 26:
        return False
    else:
        return True


stringer = input("Enter the string ")
if (pangramChecker(stringer) == True):
    print(True)
else:
    print(False)
