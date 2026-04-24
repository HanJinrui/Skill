import math

def check(ch):
	return ch not in 'aeiou'

def find(s):
	j = 0
	for i in range(len(s)):
		if check(s[i]):
			j = i
			break
	for i in range(i + 1, len(s)):
		if check(s[i]):
			if i - j < 3:
				return False
			j = i
	return True
for _ in range(int(input())):
	n = int(input())
	l = []
	(a, b) = ([], [])
	for __ in range(n):
		s = input()
		if find(s):
			a.append(s)
		else:
			b.append(s)
	k1 = len(a)
	k2 = len(b)
	(ra, rb) = (1, 1)
	(la, lb) = (0.0, 0.0)
	for ch in 'qwertyuiopasdfghjklzxcvbnm':
		(x, fx) = (0, 0)
		for s in a:
			if ch in s:
				x += 1
				fx += s.count(ch)
		if x > 0:
			la += math.log10(x) - k1 * math.log10(fx)
		(y, fy) = (0, 0)
		for s in b:
			if ch in s:
				y += 1
				fy += s.count(ch)
		if y > 0:
			lb += math.log10(y) - k2 * math.log10(fy)
	if la - lb > 7.0:
		print('Infinity')
	else:
		print('{0:.7f}'.format(pow(10, la - lb)))
	pass
