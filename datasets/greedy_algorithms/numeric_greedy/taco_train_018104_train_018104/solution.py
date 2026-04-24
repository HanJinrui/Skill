for i in range(int(input())):
	(n, x, *l) = map(int, input().split() + input().split())
	print((sum(l) + x - 1) // x, sum([(a + x - 1) // x for a in l]))
