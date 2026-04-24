n = int(input())
g = [set() for _ in range(26)]
t = [0] * 26
a = input()
for _ in range(1, n):
	b = input()
	j = 0
	while j < min(len(a), len(b)) and a[j] == b[j]:
		j += 1
	if j < min(len(a), len(b)) and a[j] != b[j]:
		g[ord(a[j]) - ord('a')].add(ord(b[j]) - ord('a'))
	elif len(a) > len(b):
		print('Impossible')
		exit()
	a = b
o = []

def dfs(x):
	t[x] = 1
	for j in g[x]:
		if t[j] == 1:
			print('Impossible')
			exit()
		if t[j] == 0:
			dfs(j)
	t[x] = 2
	o.append(chr(x + ord('a')))
for i in range(26):
	if t[i] == 0:
		dfs(i)
print(''.join(reversed(o)))
