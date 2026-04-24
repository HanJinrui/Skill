arr = [tuple(map(int, input().split())) for _ in range(int(input()))]
arr = list(enumerate(arr, 1))
while len(arr):
	p = arr[0]
	q = sorted(arr, key=lambda i: abs(p[1][0] - i[1][0]) + abs(p[1][1] - i[1][1]) + abs(p[1][2] - i[1][2]))[1]
	print(p[0], q[0])
	arr.remove(p)
	arr.remove(q)
