for _ in range(int(input())):
	input()
	k = input()
	yes = len(k) % 3 != 2
	yes &= k[1::3] == k[2::3]
	print('YES' if yes else 'NO')
