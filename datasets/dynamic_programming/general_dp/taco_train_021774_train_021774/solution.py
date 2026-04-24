t = int(input())
while t:
	t=t-1
	n,k = list(map(int,input().split()))
	a = list(map(int,input().split()))
	r = [0]*(n)
	for i in range(n):
		if i==0:
			r[i]=max(0,a[i])
		elif i<(k+1):
			r[i] = 	max(r[i-1],a[i])
		else:
			r[i] = max(r[i-1],a[i]+r[i-k-1])
	print(r[n-1])
