def read():
	s = ''
	while not s.strip().isdigit():
		s = input()
	return int(s)

def tile(i, j):
	return 2 ** (i + j) if i % 2 else 0
n = read()
for i in range(n):
	for x in [tile(i, j) for j in range(n)]:
		print(x, end=' ')
	print('', flush=True)
q = read()
for qx in range(q):
	k = read()
	i = n - 1
	j = n - 1
	ans = []
	while i > 0 or j > 0:
		ans.append((i + 1, j + 1))
		k -= tile(i, j)
		if i == 0:
			j -= 1
		elif j == 0:
			i -= 1
		elif i % 2 and k & tile(i, j - 1) or (i % 2 == 0 and k & tile(i - 1, j) == 0):
			j -= 1
		else:
			i -= 1
	ans.append((1, 1))
	for x in reversed(ans):
		print(f'{x[0]} {x[1]}')
	print('', flush=True)
