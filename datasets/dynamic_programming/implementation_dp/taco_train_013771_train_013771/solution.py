(n, h, l, r) = map(int, input().split())
arr = list(map(int, input().split()))
d = [0] + [-float('inf')] * (h - 1)
for i in range(n):
	d = [max(d[(j - arr[i]) % h], d[(j - arr[i] + 1) % h]) + int(l <= j <= r) for j in range(h)]
print(max(d))
