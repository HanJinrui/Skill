n = int(input())
m = list(map(int, input().split()))
for i in range(n):
	p = m[i]
	print(min(abs(p - m[i - 1]), abs(m[i - n + 1] - p)), max(p - m[0], m[n - 1] - p))
