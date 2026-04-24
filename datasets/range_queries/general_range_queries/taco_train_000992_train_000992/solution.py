for _ in range(int(input())):
	n = int(input())
	s = input()
	(x, y) = map(int, input().split())
	li = []
	E = [min(x, 3 * y), 0, min(3 * x, y), min(2 * x, 2 * y)]
	W = [min(3 * x, y), min(2 * x, 2 * y), min(x, 3 * y), 0]
	data = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
	for i in s:
		li.append([E[data[i]], W[data[i]]])
	res = sum([i[1] for i in li])
	mini = res
	for i in li:
		res = res - i[1] + i[0]
		mini = min(res, mini)
	print(mini)
