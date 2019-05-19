import io
import os

# lines = io.open('Newer.txt', encoding='UTF-8').read().strip().split('\n')

# for i in lines:
#     print(i)


with open('new.txt', 'r') as f:
    n = open('Newer.txt', 'w')

    for i in f:
        if not '}' in i:
            s = i.rstrip('\n')
        else:
            s = i

        if '}' in s:
            s = s.rstrip('}\n')
            s = s + '\n'
        if '{' in s:
            s = s.lstrip('{')

        n.write(s)

    n.close()

with open('Newer.txt', 'r') as f:
    n = open('Newer01.txt', 'w')

    x = 1
    for i in f:
        if x % 2 == 0:
            n.write(':' + i)
        else:
            n.write(i.rstrip('\n'))
        x += 1
