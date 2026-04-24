def rec(c, i, w, a):
	j = i + 1
	r = []
	if i >= len(w):
		return ['']
	while i < len(w) and j <= len(w):
		if w[i:j] in a and c[j] != 'WRONG PASSWORD':
			return w[i:j] + ' ' + c[j]
		else:
			j += 1
	return 'WRONG PASSWORD'
t = int(input())
for _ in range(t):
	u = int(input())
	a = input().split()
	w = input()
	c = [''] * len(w) + ['']
	for i in range(len(w) - 1, -1, -1):
		c[i] = rec(c, i, w, a)
	print(c[0])
