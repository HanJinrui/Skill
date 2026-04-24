import fractions as f

def i():
	return list(map(int, input().split()))
(n, m) = i()
a = f.gcd(m, n)
p = i()
q = i()
b = len(p)
z = set()
for e in q:
	p.append(e)
for i in range(len(p) - 2):
	z.add(p[i + 1 + min(1, (i + 1) // b)] % a)
print(['No', 'Yes'][len(z) == a])
