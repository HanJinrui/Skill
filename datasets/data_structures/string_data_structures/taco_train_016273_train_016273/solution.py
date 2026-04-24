import re
T = int(input())
for i in range(T):
	N = int(input())
	B = input()
	if re.match('^.*1([0][0])*1.*$', B):
		print('1')
	else:
		print('2')
