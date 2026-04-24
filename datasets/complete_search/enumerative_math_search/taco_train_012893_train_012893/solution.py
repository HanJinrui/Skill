(a, b, n) = map(int, input().split())
for x in range(-1000, 1001):
	if a * x ** n == b:
		exit(print(x))
print('No solution')
