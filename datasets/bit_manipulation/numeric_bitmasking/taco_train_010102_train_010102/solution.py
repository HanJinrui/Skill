p = []
for i in range(1, 10005):
	k = bin(i).replace('0b', '')
	if k == k[::-1]:
		p.append(i)
p = p[::-1]
for _ in range(int(input())):
	n = int(input())
	if n <= 12:
		print(n)
		for i in range(n):
			print(1, end=' ')
		print()
	else:
		r1 = 0
		r2 = []
		while n > 0:
			for i in range(len(p)):
				if n >= p[i]:
					r1 = r1 + n // p[i]
					r2.append([p[i], n // p[i]])
					n = n % p[i]
		print(r1)
		for i in r2:
			k = [i[0]] * i[1]
			print(*k, sep=' ', end=' ')
		print()
