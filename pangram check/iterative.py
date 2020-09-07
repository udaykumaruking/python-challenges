def pangramChecker(str):
    str = str.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for char in alpha:
        if char not in str:
            return False
    return True


string = input("Enter the string")
if (pangramChecker(string) == True):
    print(True)
else:
    print(False)
