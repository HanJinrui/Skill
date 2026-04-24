for te in [0] * int(input()):
	input()
	r = [*map(int, input().split())]
	print(r.index(min(r)) + 1, r.index(max(r)) + 1)
