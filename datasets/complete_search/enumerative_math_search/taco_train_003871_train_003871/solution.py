t = int(input())
for i in range(t):
	s1 = input()
	s2 = input()
	if s1.count('0') == s2.count('0'):
		print('Pass')
	else:
		print('Fail')
