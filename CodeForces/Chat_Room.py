import sys

inf = sys.stdin

string = str(inf.readline()).strip()

lst = ''

for i in range(len(string)):
    if lst == '' and string[i] == 'h':
        lst += 'h'
    elif lst == 'h' and string[i] == 'e':
        lst += 'e'
    elif lst == 'he' and string[i] == 'l':
        lst += 'l'
    elif lst == 'hel' and string[i] == 'l':
        lst += 'l'
    elif lst == 'hell' and string[i] == 'o':
        lst += 'o'
        break

print('YES' if lst == 'hello' else 'NO')
#
# curr = string[0]
# double_l = False
#
# lst.append(curr)
#
# for i in range(1, len(string)):
#     if curr != string[i]:
#         lst.append(string[i])
#         curr = string[i]
#         double_l = False
#     if curr == 'l' and string[i] == 'l' and not double_l:
#         lst.append('l')
#         double_l = True
#
# new_string = ''.join(lst)
#
# print('YES' if 'hello' in new_string else 'NO')
