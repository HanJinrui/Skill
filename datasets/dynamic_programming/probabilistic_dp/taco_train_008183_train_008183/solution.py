for tc in range(int(input())):
	n = int(input())
	print(n * sum((1 / x for x in range(1, n + 1))))
