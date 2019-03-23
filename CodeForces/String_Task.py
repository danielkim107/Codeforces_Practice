import sys


inf = sys.stdin

word = str(inf.readline()).lower().strip()
new_word = ''

for i in range(len(word)):
    char = word[i]
    if char in ['a', 'e', 'i', 'o', 'u', 'y']:
        continue
    else:
        new_word = new_word + '.' + word[i]
print(new_word)
