import itertools
(n, m) = map(int, input().split())

def gen(s, d):
	ans = []
	a = int(str(s), 2)
	A = int(a)
	for i in itertools.combinations(list(range(n)), d):
		c = A
		for e in i:
			c = c ^ 1 << e
		ans.append(c)
	return ans
(a, b) = map(int, input().split())
cur = gen(a, b)
for i in range(m - 1):
	(a, b) = map(int, input().split())
	cur = [x for x in cur if bin(x ^ int(str(a), 2)).count('1') == b]
print(len(cur))
