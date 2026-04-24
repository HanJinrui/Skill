(n, a, b) = map(int, input().split())
s = input()
if n * a <= len(s) <= n * b:
	(x, y) = divmod(len(s), n)
	j = 0
	for i in range(n):
		print(s[j:j + x + (y > i)])
		j = j + x + (y > i)
else:
	print('No solution')
