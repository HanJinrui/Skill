def pallan(n):
	n = str(n)
	x = 0
	s = ''
	for i in n:
		x += int(i)
		s += chr(int(i) + 97)
	s = s * x
	s = s[:x]
	if s == s[::-1]:
		return True
	return False
