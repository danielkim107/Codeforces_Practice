import sys

inf = sys.stdin

string = str(inf.readline()).strip()

if string.isupper():
    print(string.lower())
elif string[0].islower() and string[1:].isupper():
    print(string[0].upper() + string[1:].lower())
elif len(string) == 1 and string.islower():
    print(string.upper())
else:
    print(string)
