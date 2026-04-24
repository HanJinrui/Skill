(a, b, m) = map(int, input().split())
k = s = 10 ** 9 % m
i = 0
while k and i < a:
	i += 1
	if k < m - b:
		exit(print(1, str(i).zfill(9)))
	k += s
	if k >= m:
		k -= m
print(2)
