for _ in range(int(input())):
	input()
	a = set(map(int, input().split()))
	print(len(a) if min(a) else len(a) - 1)
