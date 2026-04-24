d = {2 ** i: chr(i + 97) for i in range(26)}
import math
for _ in range(int(input())):
	(n, k) = map(int, input().split())
	l = []
	a = 0
	for i in range(26):
		if k & 1 << i:
			l.append(1 << i)
			a += 1
	if n < a:
		print(-1)
	elif k == n:
		print('a' * n)
	elif a == n:
		answer = ''
		for i in range(a):
			answer += chr(int(math.log(l[i], 2) + 97))
		print(answer)
	else:
		l = []
		temp = k
		while temp:
			maximum = temp & ~(temp - 1)
			l.append(maximum)
			temp -= maximum
		if n < len(l) or n > k:
			print(-1)
			continue
		elif n == len(l):
			answer = ''
			for element in l:
				answer += d[element]
			print(answer)
		else:
			l = sorted(l)
			temp = []
			while len(l) + len(temp) != n:
				x = l.pop(0)
				if x == 1:
					temp.append(1)
					continue
				if x // 2 == 1:
					temp.append(1)
					temp.append(1)
				else:
					l = [x // 2, x // 2] + l
			l += temp
			answer = ''
			for element in l:
				answer += d[element]
			print(answer)
