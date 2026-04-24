for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	rem = set()
	for x in a:
		while x % 10 and x % 10 != 2:
			x += x % 10
		if x % 10:
			x %= 20
		rem.add(x)
	print('Yes' if len(rem) == 1 else 'No')
