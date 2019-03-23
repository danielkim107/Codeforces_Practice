import sys

inf = sys.stdin

num = int(inf.readline())

if num % 4 == 0 or num % 7 == 0 or num % 47 == 0 or num % 74 == 0 or num % 447 == 0 or num % 474 == 0 or num % \
        477 == 0 or num % 774 == 0 or num % 747 == 0:
    print('YES')
else:
    print('NO')