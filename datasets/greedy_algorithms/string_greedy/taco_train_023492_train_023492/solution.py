flip = {'0': '1', '1': '0'}
(s, t) = (input(), input())
(n, m) = (len(s), len(t))
p = [0] * m
for i in range(1, m):
	g = p[i - 1]
	while g and t[i] != t[g]:
		g = p[g - 1]
	p[i] = g + int(t[i] == t[g])
s_cnt = {'0': s.count('0'), '1': s.count('1')}
t = t[:m - p[-1]]
res = [''] * n
for i in range(n):
	char = t[i % len(t)]
	char = char if s_cnt[char] > 0 else flip[char]
	s_cnt[char] -= 1
	res[i] = char
print(''.join(res))
