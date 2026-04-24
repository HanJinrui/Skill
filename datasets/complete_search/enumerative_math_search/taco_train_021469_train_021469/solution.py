p = lambda x: True if sum((x % i == 0 for i in range(2, int(x ** 0.5) + 1))) == 0 else False
n = int(input())
if n in {3, 5}:
	print(1, '\n', n)
	quit()
for i in range(2, 100000):
	j = n - i - 3
	if j > 1 and p(i) and p(j):
		print(3, '\n', 3, i, j)
		quit()
