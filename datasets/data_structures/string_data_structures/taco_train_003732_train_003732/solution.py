from collections import defaultdict
t = int(input())
for _ in range(t):
	s = input()
	h = defaultdict(list)
	for i in range(len(s)):
		h[s[i]].append(i + 1)
	c = 0
	for i in set(s):
		if len(h[i]) % 2 == 1:
			c = c + 1
	r1 = []
	r2 = []
	o = []
	if c <= 1:
		for i in set(s):
			l = h[i]
			if len(l) % 2 == 0:
				r1 = r1 + l[:len(l) // 2]
				r2 = r2 + l[len(l) // 2:]
			else:
				o = o + h[i]
		print(*r1[::-1] + o + r2)
	else:
		print(-1)
