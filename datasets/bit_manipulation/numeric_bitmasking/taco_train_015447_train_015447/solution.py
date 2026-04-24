for _ in range(int(input())):
	n = int(input())
	a = input()
	b = input()
	if a == b:
		print('YES')
	elif '1' in a and ('00' in b or '11' in b):
		print('YES')
	else:
		print('NO')
