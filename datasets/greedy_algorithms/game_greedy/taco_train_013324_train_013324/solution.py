r = ('Alice', 'Bob')
R = lambda : max(map(int, input().split()))
for _ in [0] * R():
	R()
	a = R()
	R()
	b = R()
	print(r[a < b], '\n', r[a <= b])
