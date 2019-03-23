import sys


inf = sys.stdin

temp = inf.readline()
NK = [int(i) for i in temp.split(' ')]
n = NK[0]
k = NK[1]
temp = inf.readline()
score_lst = [int(i) for i in temp.split(' ')]

score = score_lst[k - 1]

print(sum(i >= score for i in score_lst) if score > 0 else sum(i > score for i in score_lst))
