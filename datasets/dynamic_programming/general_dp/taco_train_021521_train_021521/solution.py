def split_freq(n, s):
	freqs = [[0] * 26 for i in range(n + 1)]
	hash_pos = []
	for i in range(1, n + 1):
		c = s[i - 1]
		for j in range(26):
			freqs[i][j] = freqs[i - 1][j]
		if c == '#':
			hash_pos.append(i)
		else:
			freqs[i][ord(c) - ord('a')] += 1
	return (freqs, hash_pos)

def solve(s):
	n = len(s)
	(freqs, hash_pos) = split_freq(n, s)
	l = len(hash_pos)
	res = 0
	for i in range(l - 2):
		p1 = max(freqs[hash_pos[i]])
		if p1 == 0:
			continue
		p2 = max((ai - bi for (ai, bi) in zip(freqs[hash_pos[i + 1]], freqs[hash_pos[i]])))
		if p2 == 0:
			continue
		p3 = max((ai - bi for (ai, bi) in zip(freqs[hash_pos[i + 2]], freqs[hash_pos[i + 1]])))
		if p3 == 0:
			continue
		p4 = max((ai - bi for (ai, bi) in zip(freqs[n], freqs[hash_pos[i + 2]])))
		if p4 == 0:
			continue
		res = max(res, p1 + p2 + p3 + p4 + 3)
	return res
t = int(input().strip())
for _ in range(t):
	s = input().strip()
	print(solve(s))
