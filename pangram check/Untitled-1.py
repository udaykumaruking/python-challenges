import string
punSet = set(string.punctuation)
sett = {'.', '%', '&', '"', '!', ',', '[', '=', ':', ';', '`', '\\', '?', '('}
punSet = punSet - sett
print(punSet)
