print(3 ** sum((6 - bin({'-': 62, '_': 63}.get(c, ord(c) - 7 * (c > '9') - 6 * (c > 'Z') - 48)).count('1') for c in input())) % 1000000007)
