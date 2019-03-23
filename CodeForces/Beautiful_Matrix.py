import math
import sys

inf = sys.stdin

row = 0
col = 0

for i in range(5):
    temp = inf.readline()
    line = [int(i) for i in temp.split(' ')]
    if 1 in line:
        row = i
        col = line.index(1)
print(int(math.fabs(2 - row) + math.fabs(2 - col)))
