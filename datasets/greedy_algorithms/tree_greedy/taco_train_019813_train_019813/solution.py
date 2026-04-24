n = int(input())
p = list(map(int, input().split()))
used = [False] * n
print(p[0])
last_v = n - 1
for (i, j) in enumerate(p):
	used[j - 1] = True
	while used[last_v]:
		last_v -= 1
	if i == n - 2 or used[p[i + 1] - 1]:
		print(f'{j} {last_v + 1}')
		used[last_v] = True
	else:
		print(f'{p[i + 1]} {j}')
