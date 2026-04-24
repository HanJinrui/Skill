T = int(input())
for i in range(T):
	(n, k) = map(int, input().split())
	a = list(map(int, input().split()))
	b = [sum(a[0:k])]
	for i in range(0, len(a) - k):
		b.append(b[-1] - a[i] + a[i + k])
	m = min(b)
	print(int(sum(a) + m * (m + 1) / 2 - m))
