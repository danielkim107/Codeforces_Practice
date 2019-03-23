import sys


inf = sys.stdin

T = int(inf.readline())

for i in range(T):
    word = str(inf.readline()).strip()
    if len(word) <= 10:
        print(word)
    else:
        print(word[:1] + str(len(word) - 2) + word[-1:])
