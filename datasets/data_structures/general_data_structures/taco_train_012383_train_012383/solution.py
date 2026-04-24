n = int(input())
a = tuple(map(int, input().split()))
b = 0
(c, at) = max(((h, k) for (k, h) in enumerate(a)))
last = c
count = 0
d = list()
e = d.append
f = d.pop
for at in range(at - 1, at - n, -1):
	current = a[at]
	while current > last:
		b += count
		(last, count) = f()
	if current == last:
		count += 1
		b += count
	else:
		b += 1
		e((last, count))
		last = current
		count = 1
e((last, count))
end = len(d)
b += sum((d[k][1] for k in range(1 if d[0][1] else 2, end)))
print(b)
