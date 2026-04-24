from sys import stdin, stdout
(n, k) = map(int, stdin.readline().split())
values = list(map(int, stdin.readline().split()))
if sum(values) < k:
	stdout.write('-1')
elif sum(values) > k:
	l = 0
	r = k + 1
	while r - l > 1:
		m = (r + l) // 2
		cnt = 0
		for i in range(n):
			cnt += min(values[i], m)
		if cnt > k:
			r = m
		else:
			l = m
	for i in range(n):
		k -= min(values[i], l)
		values[i] -= min(values[i], l)
	i = 0
	while k:
		if values[i]:
			values[i] -= 1
			k -= 1
		i = (i + 1) % n
	for j in range(i, i + n):
		if values[j % n]:
			stdout.write(str(j % n + 1) + ' ')
