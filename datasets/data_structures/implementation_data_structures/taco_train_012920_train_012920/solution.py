def solve(a):
	l, r = 0, 0
	d = {}
	for ii in a:
		d[ii] = 0
	i = 0
	n = len(a)
	best = 0
	bestl, bestr = 0, 0
	dist = 0
	while r<n:
		d[a[r]]+=1
		if d[a[r]]==2:
			while d[a[r]]!=1:
				d[a[l]]-=1
				l+=1
		if (r-l)>best:
			bestl = l
			bestr = r
			best = r-l
		r+=1

	print(bestl+1, bestr+1)
	
for ii in range(eval(input())):
	n = eval(input())
	a = list(map(int, input().split()))
	#for ii in a: d[ii]=0
	solve(a)
