for _ in range(int(input())):
	S1 = set()
	S2 = set()
	q = int(input())
	for i in range(q):
		n = int(input())
		if n not in S1:
			for j in S1:
				S2.add(n ^ j)
			S1.add(n)
			S1 = S1.union(S2)
			O = 0
			e = 0
			for j in S1:
				cnt = bin(j).count('1')
				if cnt % 2 == 0:
					e += 1
				else:
					O += 1
		print(e, O)
