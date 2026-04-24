for _ in range(int(input())):
	K = int(input().split()[1])
	print(max([K // int(a) * int(b) for (a, b) in zip(input().split(), input().split())]))
