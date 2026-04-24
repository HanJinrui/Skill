for i in range(int(input())):
	[l, r] = [int(i) for i in input().split()]
	print('Odd' if (r + r % 2 - l + l % 2) // 2 % 2 else 'Even')
