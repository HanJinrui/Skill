t = int(input())
for _ in range(t):
	n = int(input())
	s = input()
	i = s.find('1')
	s = s[i:] + s[:i]
	o = s.split('1')
	result = sum(map(len, o)) - max(map(len, o))
	print(result)
