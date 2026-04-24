t = int(input())
for _ in range(t):
	n = int(input())
	l = list(map(int, input().split()))
	pref = [0] * (n + 2)
	last = [0] * (n + 1)
	for i in l:
		last[i] += 1
	(index, m) = (0, 0)
	for i in l:
		index += last[i - 1]
		index -= pref[i + 1]
		pref[i] += 1
		last[i] -= 1
		m = max(m, index)
	print(m)
