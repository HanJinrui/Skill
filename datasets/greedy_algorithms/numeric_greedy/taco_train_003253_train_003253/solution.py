for _ in [0] * int(input()):
	print(2022 * (int(input()) - 1 + __import__('math').prod(map(int, input().split()))))
