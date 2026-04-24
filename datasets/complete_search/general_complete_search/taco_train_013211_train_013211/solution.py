I = lambda : map(int, input().split())
(n, m, k) = I()
m += 2
A = set()
for i in range(k):
	(x, y) = I()
	a = x * m + y
	if {a - m - 1, a - m, a - 1} <= A or {a - m, a - m + 1, a + 1} <= A or {a - 1, a + m - 1, a + m} <= A or ({a + 1, a + m, a + m + 1} <= A):
		print(i + 1)
		break
	A.add(a)
else:
	print(0)
