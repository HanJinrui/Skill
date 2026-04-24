for _ in range(eval(input())):
	n, _ = (int(x) for x in input().split())
	best = ''.join(min(sorted(c)[n >> 1], sorted(c)[n - 1 >> 1]) 
				   for c in zip(*(input() for _ in range(n))))
	print(best)
