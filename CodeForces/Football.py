import sys


inf = sys.stdin

lineup = str(inf.readline()).strip()

if len(lineup) < 7:
    print('NO')
else:
    print('YES' if '1111111' in lineup or '0000000' in lineup else 'NO')
