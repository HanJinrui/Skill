def g(f):
	a = b = 0
	for _ in range(f):
		i = input()
		(a, b) = (a ^ int(i.replace(' ', ''), 2), b * 2 + i.count('1') % 2)
	return (a, b)
n = int(input().split()[0])
print('Yes' if g(n) == g(n) else 'No')
