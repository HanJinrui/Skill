def parse(i):
	t = input().split()
	return (int(t[0]), int(t[1]), i)
(n, m) = [int(x) for x in input().split()]
list = [parse(i) for i in range(m)]
list.sort(key=lambda x: (x[0], -x[1]))
f = 0
t = 1
fakeFrom = 1
fakeTo = 2
graph = []
for i in range(m):
	if list[i][1] == 1:
		graph.append((f + 1, t + 1, list[i][2]))
		t += 1
	else:
		graph.append((fakeFrom + 1, fakeTo + 1, list[i][2]))
		if fakeTo >= t:
			print(-1)
			exit(0)
		fakeFrom += 1
		if fakeFrom == fakeTo:
			fakeFrom = 1
			fakeTo += 1
graph.sort(key=lambda x: x[2])
for x in graph:
	print(x[0], x[1])
