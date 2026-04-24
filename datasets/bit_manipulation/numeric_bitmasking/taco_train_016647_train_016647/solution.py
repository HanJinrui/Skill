xd = [2, 3, 0, 9]
for _ in range(int(input())):
	n = int(input())
	n = len(bin(n)) - 3
	if n == 0:
		print(0)
	elif n == 1:
		print(1)
	else:
		n -= 2
		print(xd[n % 4])
