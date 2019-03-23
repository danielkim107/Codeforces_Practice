import sys

inf = sys.stdin

num = int(inf.readline())

color = str(inf.readline()).strip()

counter = 0

prev = color[0]

for i in range(1, num):
    if color[i] == prev:
        counter += 1
    else:
        prev = color[i]

print(counter)
