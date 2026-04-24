I = lambda : map(int, input().split())
(n, k) = I()
c = 0
for z in sorted(I()):
	if z <= k:
		k -= z
		c += 1
print(c)
