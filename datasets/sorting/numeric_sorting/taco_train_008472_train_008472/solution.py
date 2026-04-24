(n, a, b) = map(int, input().split())
(x, *l) = map(int, input().split())
l.sort()
c = 0
s = sum(l)
p = x * a / b - x
while p < s:
	c += 1
	s -= l.pop()
print(c)
