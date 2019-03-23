import sys

inf = sys.stdin

T = inf.readline()
counter = 0

for i in range(int(T)):
    temp = inf.readline()
    capability = [int(i) for i in temp.split(' ')]
    if sum(capability) >= 2:
        counter += 1
print(counter)