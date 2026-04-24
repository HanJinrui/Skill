import re
t = int(input())
for i in range(t):
	password = input()
	lower = re.search('[a-z]', password)
	upper = re.search('[A-Z]', password[1:-1])
	digit = re.search('[0-9]', password[1:-1])
	special = re.search('[@#$%&?]', password[1:-1])
	if len(password) >= 10 and lower and upper and digit and special:
		print('YES')
	else:
		print('NO')
