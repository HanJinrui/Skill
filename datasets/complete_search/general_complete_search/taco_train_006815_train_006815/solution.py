for i in range(int(input())):
	k = list(map(int, input().split()))
	print(1) if len(set(k)) == 2 else print(0)
