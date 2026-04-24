for _ in range(int(input())):
	input()
	a = list(map(int, input().split()))
	print(('NO', 'YES')[sorted(a)[::2] == sorted(a[::2])])
