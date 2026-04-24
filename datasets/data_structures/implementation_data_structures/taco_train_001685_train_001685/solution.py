(n, t, c) = map(int, input().split())
k = r = 0
for i in input().split():
	k = k + 1 if int(i) <= t else 0
	r += k >= c
print(r)
