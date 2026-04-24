t = int(input())
for i in range(t):
	n = int(input())
	arr = list(map(int, input().split()))[::-1]
	s = [1]
	for i in range(1, n):
		if arr[i] * arr[i - 1] < 0:
			s.append(s[-1] + 1)
		else:
			s.append(1)
	print(*s[::-1])
