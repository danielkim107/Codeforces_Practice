import sys


inf = sys.stdin

word = str(inf.readline()).strip()

print(word[:1].capitalize() + word[1:])
