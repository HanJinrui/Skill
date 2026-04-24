(n, m, k) = map(int, input().split())
s = [input() for _ in range(n)]
if k > 1:
	s += [''.join(t) for t in zip(*s)]
summ = 0
for i in range(len(s)):
	summ += sum([len(t) - k + 1 for t in s[i].split('*') if len(t) >= k])
print(summ)
