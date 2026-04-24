for _ in range(int(input())):
	C = 0
	input().split()
	a = str(input())
	b = str(input())
	a = a + b[::-1]
	for i in range(len(a) - 1):
		if a[i] == a[i + 1]:
			C += 1
	print('YNEOS'[C > 1::2])
