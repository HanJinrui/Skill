for _ in range(int(input())):
	n = int(input())
	s = sorted(list(map(int, input().split())))
	for i in range(n):
		print(s[i], s[-i - 1], end=' ')
	print()
