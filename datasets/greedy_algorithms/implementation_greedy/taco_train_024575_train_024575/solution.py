s = ['.', '@', '%']
for i in input():
	if s[-1] == i and (s[-2] == i or s[-2] == s[-3]):
		s.pop()
	s.append(i)
print(''.join(s[3:]))
