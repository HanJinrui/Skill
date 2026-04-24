(n, k) = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
z = max(r[-1] - c[-1], 0)
if k == 0:
	best = z
	acc = 0
	for i in range(n - 1, -1, -1):
		acc += r[i]
		best = max(best, acc - c[i])
	print(best)
elif k > 1:
	print(max(sum(r) - min(c[:-1]), z))
else:
	best = max(z, sum(r) - sum(sorted(c)[:2]), sum(r[:-1]) - min(c[:-1]), sum(r) - min(r[1:]) - c[0])
	acc = 0
	for i in range(n - 1, 0, -1):
		acc += r[i]
		best = max(best, acc - c[i])
	print(best)
