for _ in range(int(input())):
	n = int(input())
	print(n if n % 4 == 3 or n % 4 == 0 else n - 1)
