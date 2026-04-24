n = int(input().strip())
a = [int(i) for i in input().strip().split()]
s = []
_max = 0
for i in a:
	while len(s) > 0:
		_max = max(_max, s[-1] ^ i)
		if i < s[-1]:
			s.pop()
		else:
			break
	s.append(i)
print(_max)
