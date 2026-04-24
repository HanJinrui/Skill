(n, k) = map(int, input().split())
(s, t) = ('', '01'[n > 1])
for c in input():
	s += (c, t)[k > 0]
	k -= c > t
	t = '0'
print(s)
