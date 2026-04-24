(n, k) = [int(x) for x in input().split()]
s = set((int(x) for x in input().split()))
r = 0
for x in s:
	if x - k in s:
		r += 1
print(r)
