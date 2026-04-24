from functools import *
print(''.join(sorted([input() for _ in range(int(input()))], key=cmp_to_key(lambda x, y: 2 * (x + y > y + x) - 1))))
