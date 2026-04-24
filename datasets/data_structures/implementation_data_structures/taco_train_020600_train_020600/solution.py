for i in range(int(input())):
	num = int(input())
	a = [j for k in range(num) for j in input().split()]
	x = set(a[::2])
	y = set(a[1::2])
	print(len(x) + len(y))
