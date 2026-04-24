n = int(input())
k = ['o'] * n
a = b = 1
while b <= n:
	k[b - 1] = 'O'
	(a, b) = (b, a + b)
print(*k, sep='')
