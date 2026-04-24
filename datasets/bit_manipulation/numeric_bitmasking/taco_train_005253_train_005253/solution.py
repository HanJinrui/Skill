import math
for _ in range(int(input())):
	n = int(input())
	if n == 1:
		print(1, 1, sep='\n')
	elif n & 1 == 1:
		print(-1)
	else:
		print(*list(range(1, n + 1))[::-1])
		s1 = ''
		d = {}
		for i in range(n, 0, -1):
			try:
				s1 += str(d[i]) + ' '
			except:
				c = (1 << int(math.log(i, 2)) + 1) - (i + 1)
				d[c] = i
				s1 += str(c) + ' '
		print(s1)
