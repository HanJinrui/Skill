t = int(input())
for ni in range(t):
	(n, a, b, c) = map(int, input().split())
	f = [int(i) for i in input().split()]
	l = [abs(b - i) + abs(i - a) for i in f]
	print(min(l) + c)
