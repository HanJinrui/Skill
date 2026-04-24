for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	c = 0
	s = 0
	for j in range(n):
		s = s + arr[j]
		if s == (j + 1) * (j + 2) // 2:
			c += 1
	print(c)
