for _ in range(int(input())):
	input()
	print('YES\n101\n' + ' '.join([str(x) for x in range(101)]) if min(list(map(int, input().split()))) >= 0 else 'NO')
