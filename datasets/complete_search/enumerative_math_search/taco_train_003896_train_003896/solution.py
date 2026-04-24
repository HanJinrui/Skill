def f(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True
n = int(input())
for i in range(10, 1000000):
	if i != int(str(i)[::-1]) and f(i) and f(int(str(i)[::-1])):
		n -= 1
	if n == 0:
		print(i)
		break
