t = int(input())
while t > 0:
	(n, k) = list(map(int, input().split()))
	st = []
	for i in range(n):
		st.append(input())
	q = [0]
	dist = [-1] * n
	while len(q) > 0:
		pos = q.pop(0)
		for i in range(max(0, pos - k), min(n, pos + k + 1)):
			if st[pos][i] == '1' and dist[i] == -1:
				q.append(i)
				dist[i] = dist[pos] + 1
	print(dist[n - 1])
	t -= 1
