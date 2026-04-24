from bisect import bisect_left

def Smallestonleft(a, n):
	b = [-1] * n
	l = [a[0]]
	for i in range(1, n):
		j = bisect_left(l, a[i])
		if j:
			b[i] = l[j - 1]
		l.insert(j, a[i])
	return b
