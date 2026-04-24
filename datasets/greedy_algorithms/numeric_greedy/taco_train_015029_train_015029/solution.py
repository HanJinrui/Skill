(k, a, b, v) = map(int, input().split())
o = 0
while a > 0:
	o += 1
	a -= v * min(b + 1, k)
	b -= min(b, k - 1)
print(o)
