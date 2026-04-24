for i in range(int(input())):
	(n, x) = map(int, input().split())
	a = min(map(int, input().split()))
	print(max(n, x // a + (x % a != 0)))
