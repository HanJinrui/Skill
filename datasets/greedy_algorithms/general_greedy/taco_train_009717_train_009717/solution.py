for _ in '0' * int(input()):
	input()
	print(sum(map(int, input().split())) + sum(sorted([*map(int, input().split())])[:-1]))
