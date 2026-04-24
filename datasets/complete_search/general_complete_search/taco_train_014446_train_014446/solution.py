f = lambda : map(int, input().split())
(n, m, k) = f()
a = list(f())
s = m * n
for i in range(n):
	for b in f():
		i = a.index(b)
		s += i
		a = [a.pop(i)] + a
print(s)
