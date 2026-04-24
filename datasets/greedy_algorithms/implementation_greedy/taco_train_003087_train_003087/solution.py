n = int(input())
s = input()
(l, r) = (s.rfind('L') + 1, s.find('R') + 1)
if r > 0:
	print(r, r + s.count('R'))
else:
	print(l, l - s.count('L'))
