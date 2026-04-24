n = int(input())
_ = input()
d = list(map(int, input().split()))
m = -n
z = -1
for (i, v) in enumerate(d):
	if not v:
		z = -1
		continue
	if z >= 0 and v != i - z + 1:
		z = -1
	elif v == 1:
		z = i
		y = m
	m = max(m, i - v + 2)
if z == 0:
	print(0)
elif z > 0 and y <= -n + z:
	print(z)
else:
	print(n + max(m, 0))
