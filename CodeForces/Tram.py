import sys

cap = 0
inf = sys.stdin

cap_lst = []

T = int(inf.readline())

for i in range(T):
    temp = inf.readline()
    tram = [int(i) for i in temp.split(' ')]
    cap = cap - tram[0]
    curr = cap + tram[1]
    cap = curr if curr > cap else cap
    cap_lst.append(cap)

print(max(cap_lst))
