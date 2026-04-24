for _ in range(int(input())):
	a = int(input())
	l = list(map(int, input().split()))
	l.sort()
	print(sum(l[::-2]))
