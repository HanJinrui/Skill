for iii in range(int(input())):
	n = int(input())
	q = list(map(int, input().split()))
	q1 = {}
	maxx = 0
	for i in range(n):
		q1 = {}
		for j in range(i + 1, n):
			x = (q[j] - q[i]) / (j - i)
			if x in q1:
				q1[x] += 1
			else:
				q1[x] = 1
		for i in q1:
			maxx = max(maxx, q1[i])
	print(n - 1 - maxx)
