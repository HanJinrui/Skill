(N, H, I) = map(int, input().split())
a = [[0] * (H + I + 1) for _ in range(N)]
for p in range(N):
	for q in list(map(int, input().split()))[1:]:
		a[p][q] += 1
for h in range(H, 0, -1):
	m = max((a[p][h + I] for p in range(N)))
	for p in range(N):
		a[p][h] += max(a[p][h + 1], m)
print(max((a[p][1] for p in range(N))))
