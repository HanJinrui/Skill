for _ in range(int(input())):
	(n, k) = map(int, input().split())
	s1 = set(range(n))
	s2 = set(range(n))
	for i in range(k):
		(r, c) = map(int, input().split())
		s1.remove(r - 1)
		s2.remove(c - 1)
	(l1, l2) = (list(s1), list(s2))
	print(n - k, end=' ')
	for i in range(len(l1)):
		print(l1[i] + 1, l2[i] + 1, end=' ')
	print()
