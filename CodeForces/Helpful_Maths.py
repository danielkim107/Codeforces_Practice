import sys


inf = sys.stdin

command = str(inf.readline()).strip()
one = command.count('1')
two = command.count('2')
three = command.count('3')
new_command = ''

for i in range(one):
    new_command += '1+'
for i in range(two):
    new_command += '2+'
for i in range(three):
    new_command += '3+'
print(new_command[:-1])
