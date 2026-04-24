def solve(l, k):
	s = [x for x in l]
	n = len(s)
	r = 0
	if k == 1:
		s0 = s[:]
		r0 = r1 = 0
		for (i, c) in enumerate(s):
			if i % 2:
				if c == '0':
					s0[i] = '1'
					r0 += 1
			elif c == '1':
				s0[i] = '0'
				r0 += 1
		s1 = s[:]
		for (i, c) in enumerate(s):
			if i % 2 == 0:
				if c == '0':
					s1[i] = '1'
					r1 += 1
			elif c == '1':
				s1[i] = '0'
				r1 += 1
		if r0 < r1:
			r = r0
			s = s0
		else:
			r = r1
			s = s1
	else:
		i = j = 0
		while j < n:
			while j < n and s[i] == s[j]:
				j += 1
			if j - i > k:
				for l in range(i + k, j, k + 1):
					if l == j - 1:
						l -= 1
					s[l] = '0' if s[l] == '1' else '1'
					r += 1
			i = j
	print(r)
	print(''.join(s))
for t in range(int(input())):
	(n, k) = [int(x) for x in input().split()]
	solve(input(), k)
