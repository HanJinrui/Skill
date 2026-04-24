(n, k) = map(int, input().split())
t = '01'[n > 1]
for c in input():
	print((c, t)[k > 0], end='')
	k -= c > t
	t = '0'
