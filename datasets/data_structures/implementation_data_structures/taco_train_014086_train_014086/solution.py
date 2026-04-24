(n, m) = map(int, input().split())
t = [int(input()) for i in range(n)]
(s, p) = (0, [0] * (n + 1))
for i in t:
	if i < 0:
		m -= 1
		p[-i] -= 1
	else:
		p[i] += 1
q = {i for i in range(1, n + 1) if p[i] == m}
if len(q) == 0:
	print('Not defined\n' * n)
elif len(q) == 1:
	j = q.pop()
	print('\n'.join(['Truth' if i == j or (i < 0 and i + j) else 'Lie' for i in t]))
else:
	q.update({-i for i in q})
	print('\n'.join(['Not defined' if i in q else 'Truth' if i < 0 else 'Lie' for i in t]))
