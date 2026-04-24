T = int(input())
for i in range(T):
	s = input()
	x = 0
	y = len(s) - 1
	z = 1
	while x <= y:
		if s[x] == '?' == s[y]:
			z = z * 26 % 10000009
		elif s[x] != '?' and s[y] != '?' and (s[x] != s[y]):
			z = 0
			break
		x += 1
		y -= 1
	print(z)
