from bisect import bisect_right
for _ in range(int(input())):
	(n, m) = map(int, input().split())
	a = list(map(int, input().split()))
	l = []
	su = 0
	r = 0
	for i in range(n):
		su += a[i]
		su %= m
		it = bisect_right(l, su)
		if it != len(l):
			r = max(r, su - l[it] + m)
			l.insert(it, su)
		else:
			r = max(r, su)
			l.append(su)
	print(r)
