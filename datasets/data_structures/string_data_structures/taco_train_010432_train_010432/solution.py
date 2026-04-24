import string

n = int(input())
d = {}
for x in string.ascii_uppercase:
	d[x] = x
for i in range(n):
	a, b = input().split()
	a, b = a.upper(), b.upper()
	d[a], d[b] = d[b], d[a]
for x in string.ascii_lowercase:
	d[x] = d[x.upper()].lower()
m = {}
for k, v in list(d.items()):
	m[v] = k
s = input()
print(''.join([m[c] if c in m else c for c in s]))
