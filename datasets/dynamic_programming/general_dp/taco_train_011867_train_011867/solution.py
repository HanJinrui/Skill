T = int(input())
while T > 0:
	T -= 1
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	for i in range(n):
		b[i] = (b[i] + 4 - a[i]) % 4
	i = n - 1
	while i > 0:
		b[i] -= b[i - 1]
		i -= 1
	ans = 0
	s2 = 0
	s3 = 0
	for i in range(n):
		if b[i] < 2:
			ans += max(b[i], 0)
			if b[i] == -2:
				s2 += 1
			if b[i] == -3:
				s3 += 1
		else:
			if s3 > 0:
				s3 -= 1
				ans += 1
				b[i] -= 4
			elif s2 > 0:
				s2 -= 1
				ans += 2
				b[i] -= 4
			ans += max(b[i], 0)
			if b[i] == -2:
				s2 += 1
			if b[i] == -3:
				s3 += 1
	print(ans)
