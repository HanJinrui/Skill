import sys
from array import array

def input():
	return sys.stdin.buffer.readline().decode('utf-8')
(n, w, m) = map(int, input().split())
w = float(w)
eps = 1e-09
req = n * w / m
cup = [req] * m
ans = [[] for _ in range(m)]
j = 0
for i in range(n):
	milk = w
	cnt = 0
	while j < m and milk > eps:
		x = min(milk, cup[j])
		milk -= x
		cup[j] -= x
		ans[j].append(f'{i + 1} {x:.8f}')
		cnt += 1
		if cup[j] < eps:
			j += 1
	if cnt > 2:
		print('NO')
		exit()
print('YES')
print('\n'.join((' '.join(line) for line in ans)))
