def asum(n):
	return n*(n+1)/2

for t in range(eval(input())):
	n = eval(input())
	low = 0
	high = 10000000000
	while low!=high:
		mid = (low+high)/2
		sm = asum(mid)
		spm = asum(mid-1)
		if sm>=n and spm<n:
			break
		if(sm<n):
			low = mid+1
		else:
			high = mid-1
	if low!=high:
		print(mid)
	else:
		print(low)
