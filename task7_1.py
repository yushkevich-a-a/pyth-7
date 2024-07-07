st = input()

newSt = ''.join(reversed(st))


if (st == newSt):
    print('Yes')
else:
    print('No')