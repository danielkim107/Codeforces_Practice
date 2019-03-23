import sys


inf = sys.stdin

first_word = str(inf.readline()).lower().strip()
second_word = str(inf.readline()).lower().strip()

if first_word == second_word:
    print(0)
elif first_word > second_word:
    print(1)
else:
    print(-1)

