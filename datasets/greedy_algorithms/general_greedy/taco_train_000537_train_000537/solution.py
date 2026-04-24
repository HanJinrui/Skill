(n, k) = [int(t) for t in input().strip().split()]
a = [int(t) for t in input().strip().split()]
r = 0
i = -k
while i + k < n:
	j = min(n - 1, i - 1 + k + k)
	while j >= i:
		if a[j]:
			break
		j -= 1
	if j <= i:
		r = -1
		break
	r += 1
	i = j
print(r)
