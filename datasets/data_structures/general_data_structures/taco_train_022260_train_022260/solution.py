def test(n, a, b):
	s = sum(a) + sum(b)
	if s % n > 0:
		return -1
	v = s // n
	for i in range(n - 1):
		if a[i] == v:
			a[i + 1] += b[i]
		elif a[i] + b[i] == v:
			pass
		elif a[i] + b[i + 1] == v:
			a[i + 1] += b[i]
			b[i + 1] = 0
		elif a[i] + b[i] + b[i + 1] == v:
			b[i + 1] = 0
		else:
			return -1
	return v
T = int(input())
for t in range(T):
	n = int(input())
	b = list(map(int, input().split()))
	a = list(map(int, input().split()))
	print(test(n, a, b))
