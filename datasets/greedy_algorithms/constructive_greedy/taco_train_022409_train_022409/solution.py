for _ in range(int(input())):
	n = int(input())
	s = input()
	print(n + sum((i for i in range(1, n) if s[i] != s[i - 1])))
