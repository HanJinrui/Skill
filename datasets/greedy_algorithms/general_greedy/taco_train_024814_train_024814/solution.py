n = input()
k = len(n) - 1
print(sum(map(int, str(int(n) - int('0' + '9' * k)))) + 9 * k)
