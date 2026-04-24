def check(s):
	p = ['00', '01', '10', '11']
	for val in s[1:-1]:
		for i in range(4):
			p[i] = p[i] + str(int(p[i][-2]) ^ int(p[i][-1]) ^ int(val))
	count = 0
	for x in p:
		if convert(x) == s:
			count += 1
			r = x
	if count == 1:
		return r
	elif count == 0:
		return 'No solution'
	else:
		return 'Multiple solutions'

def convert(s):
	s = s[-1] + s + s[0]
	n = len(s)
	result = ''
	for i in range(1, n - 1):
		if (s[i - 1] + s[i + 1]).count('1') == 1:
			result += '1' if s[i] == '0' else '0'
		else:
			result += s[i]
	return result
t = int(input())
for _ in range(t):
	s = input().rstrip()
	print(check(s))
