(n, k) = map(int, input().split())
a = input().strip()
print(n)
for j in (0, 1):
	b = (str(int(a[:k]) + j) * (n // k + 1))[:n]
	if b >= a:
		print(b)
		break
