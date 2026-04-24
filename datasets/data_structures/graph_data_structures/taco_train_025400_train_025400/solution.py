def root(i):
	while index[i] != i:
		index[i] = index[index[i]]
		i = index[i]
	return i

def union(a, b):
	if arr[a] > arr[b]:
		index[b] = a
	elif arr[b] > arr[a]:
		index[a] = b
for _ in range(int(input())):
	n = int(input())
	ar = list(map(int, input().split()))
	arr = [0] + ar
	index = [i for i in range(n + 1)]
	for t in range(int(input())):
		compete = list(map(int, input().split()))
		if compete[0] == 0:
			(x, y) = (root(compete[1]), root(compete[2]))
			if x == y:
				print('Invalid query!')
			else:
				union(x, y)
		else:
			print(root(compete[1]))
