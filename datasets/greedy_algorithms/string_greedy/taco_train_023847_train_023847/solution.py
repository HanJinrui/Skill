from sys import stdin, stdout
words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = stdin.readline().strip()
f = stdin.readline().strip()
ans = -1
d = {}
for v in s:
	if v in d:
		d[v] += 1
	else:
		d[v] = 1
for i in range(min(len(s), len(f))):
	if f[i] in d and d[f[i]]:
		d[f[i]] -= 1
	else:
		break
	for v in words:
		if v in d and d[v] and (i == len(f) - 1 or v > f[i + 1]):
			ans = i
			break
if ans == -1 and max(list(s)) > f[0]:
	s = sorted(list(s))
	first = ''
	for i in range(len(s)):
		if s[i] > f[0]:
			first += s[i]
			s[i] = '_'
			break
	first += ''.join(sorted(list(s))[1:])
elif ans == -1:
	first = '-1'
else:
	s = sorted(list(s))
	d = {}
	first = ''
	for i in range(ans + 1):
		first += f[i]
		if f[i] in d:
			d[f[i]] += 1
		else:
			d[f[i]] = 1
	for i in range(len(s)):
		if s[i] in d and d[s[i]]:
			d[s[i]] -= 1
			s[i] = '_'
	for i in range(len(s)):
		if s[i] != '_' and (ans + 1 == len(f) or s[i] > f[ans + 1]):
			first += s[i]
			s[i] = '_'
			break
	for i in range(len(s)):
		if s[i] != '_':
			first += s[i]
stdout.write(first)
