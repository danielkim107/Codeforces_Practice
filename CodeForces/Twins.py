import sys

inf = sys.stdin

string = str(inf.readline()).strip()

print(string if (string[:1].islower() and string[1:].isupper()) or (string[:1].isupper() and string[1:].islower()) else
      string.capitalize())

