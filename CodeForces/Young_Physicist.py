import sys

inf = sys.stdin

T = int(inf.readline())

first = 0
second = 0
third = 0

for i in range(T):
    temp = inf.readline()
    row = [int(i) for i in temp.split(' ')]
    first += row[0]
    second += row[1]
    third += row[2]

print('YES' if first == 0 and second == 0 and third == 0 else 'NO')
