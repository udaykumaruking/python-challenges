# import string

string1 = input("Enter the string: ")
string1 = string1
strSet = set(string1)
stringLen = len(string1)
strSetlen = len(strSet)
if stringLen == strSetlen:
    print("Unique")
else:
    print("Found Duplicates")
