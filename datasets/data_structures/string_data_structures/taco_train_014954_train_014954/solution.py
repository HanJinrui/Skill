from datetime import *
for _ in range(int(input())):
	p = input()
	P = datetime.strptime(p, '%I:%M %p')
	ans = ''
	for i in range(int(input())):
		n = input()
		L = datetime.strptime(n[:8], '%I:%M %p')
		R = datetime.strptime(n[9:], '%I:%M %p')
		if P >= L and P <= R:
			ans = ans + '1'
		else:
			ans = ans + '0'
	print(ans)
