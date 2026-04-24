for _ in range(int(input())):
	i = int(input())
	j = list(map(int, input().split()))
	print((max(j) - min(j)) * 2)
