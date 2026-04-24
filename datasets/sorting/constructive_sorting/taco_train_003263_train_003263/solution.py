input()
P = list(map(int, input().split()))
l = sorted([[P.index(p), i % 2] for (i, p) in enumerate(sorted(P))])
for (a, b) in l:
	print(b)
