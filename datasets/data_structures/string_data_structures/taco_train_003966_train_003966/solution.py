t = int(input())
for i in range(t):
	n = int(input())
	res = set(input())
	for j in range(n - 1):
		s = set(input())
		res = res.intersection(s)
	print(len(res))
