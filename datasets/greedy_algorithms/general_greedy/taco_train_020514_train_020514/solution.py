for _ in range(int(input())):
	n = int(input())
	A = input()
	B = input()
	s = set(A + B)
	l = []
	for i in s:
		a1 = A.count(i)
		b1 = B.count(i)
		l.append(min(a1, b1))
	print(max(l))
