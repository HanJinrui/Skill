from random import randint

def ask(l1, r1, l2, r2):
	print('?', r1 - l1 + 1, r2 - l2 + 1)
	for i in range(l1, r1 + 1):
		print(i + 1, end=' ')
	print()
	for i in range(l2, r2 + 1):
		print(i + 1, end=' ')
	print(flush=True)
	s = input()
	if s[0] == 'F':
		return 0
	if s[0] == 'S':
		return 1
	if s[0] == 'E':
		return 2
	exit()
for _ in range(int(input())):
	(n, k) = map(int, input().split())
	flag = 0
	for i in range(30):
		x = randint(1, n - 1)
		if ask(0, 0, x, x) == 1:
			print('!', 1)
			flag = 1
			break
	if flag:
		continue
	i = 0
	while ask(0, (1 << i) - 1, 1 << i, min(n - 1, (1 << i + 1) - 1)) == 2:
		i += 1
	(l, r) = (0, min(n - (1 << i) - 1, (1 << i) - 1))
	while l < r:
		m = l + r >> 1
		if ask(0, m, 1 << i, (1 << i) + m) == 2:
			l = m + 1
		else:
			r = m
	print('!', (1 << i) + l + 1)
