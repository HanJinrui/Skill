for i in range(int(input())):
	(a, b) = map(int, input().split())
	c1 = bin(a).count('1')
	c2 = bin(b - 1).count('1')
	ans = c2 - c1 + 1
	if a == b:
		print(0)
	elif a == 0 and b == 1:
		print(1)
	elif b == 0 or b == 1:
		print(-1)
	elif ans <= 0:
		print(2)
	else:
		print(ans)
