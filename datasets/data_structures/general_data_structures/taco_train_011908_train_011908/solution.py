import bisect
(n, k) = map(int, input().strip().split())
H = list(map(int, input().strip().split()))
assert len(H) == n
t = int(input().strip())
for _ in range(t):
	(l, r) = map(int, input().strip().split())
	h = sorted(H[l:r + 1])
	p = 0
	for (i, x) in enumerate(h):
		p += bisect.bisect_right(h, x + k, i) - i - 1
	print(p)
