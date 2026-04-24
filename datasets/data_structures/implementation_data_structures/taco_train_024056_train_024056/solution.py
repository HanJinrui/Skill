(a, b) = map(int, input().split())
z = list(map(int, input().split()))
p = z[0]
s = 0
for i in range(1, a):
	if z[i] < p:
		s += 1
	else:
		s = 1
		p = z[i]
	if s >= b:
		break
print(p)
