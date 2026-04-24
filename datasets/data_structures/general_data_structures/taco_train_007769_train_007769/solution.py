for _ in range(int(input())):
	n = int(input())
	a = [*map(int, input().split())]
	q = max(a)
	if a == [q] * n:
		print(0)
	elif a[-1] == q:
		print(1)
	else:
		print(2)
