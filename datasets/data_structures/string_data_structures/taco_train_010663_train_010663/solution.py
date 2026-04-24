import random
for x in range(int(input())):
	n = int(input())
	a = []
	for r in range(n):
		a.append(input())
	a = set(a)
	while True:
		s = ''
		for xx in range(n):
			s += str(random.randint(0, 1))
		if s not in a:
			print(s)
			break
