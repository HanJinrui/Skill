(i, n) = (0, int(input()))
s = ['pushQueue'] * n
(a, b, c) = (' popQueue', ' popStack', ' popBack')
p = ['0', '1' + a, '2' + a + b, '3' + a + b + c]
t = []
for j in range(n):
	x = int(input())
	if x:
		t.append((x, j))
		continue
	t = sorted((k for (x, k) in sorted(t)[-3:]))
	k = len(t)
	if k > 0:
		s[i:t[0]] = ['pushStack'] * (t[0] - i)
	if k > 1:
		s[t[1]] = 'pushStack'
	if k > 2:
		s[t[2]] = 'pushBack'
	(i, t, s[j]) = (j + 1, [], p[k])
print('\n'.join(s))
