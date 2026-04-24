import bisect
(n, d) = map(int, input().split())
E = list(map(int, input().split()))
count = 0
B = sorted(E[:d])
for i in range(d, n):
	median = (B[(d - 1) // 2] + B[d // 2]) / 2
	if E[i] >= 2 * median:
		count += 1
	del B[bisect.bisect_left(B, E[i - d])]
	bisect.insort_left(B, E[i])
print(count)
