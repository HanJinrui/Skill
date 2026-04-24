for it in range(int(input())):
	s = input()
	a = [ord(i) - ord('a') + 1 for i in s]
	if len(a) == 1:
		print('Bob', a[0])
	elif len(a) % 2:
		print('Alice', sum(a) - 2 * min(a[0], a[-1]))
	else:
		print('Alice', sum(a))
