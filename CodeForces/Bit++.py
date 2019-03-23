import sys

inf = sys.stdin

T = inf.readline()

counter = 0


for i in range(int(T)):
    command = str(inf.readline()).strip()
    if '+' in command:
        counter += 1
    else:
        counter -= 1
print(counter)