t=int(input())
while t:
	a=input().split()
	n=int(a[0])
	k=int(a[1])
	sum=1
	p=1
	for j in range(0,k):
		p=p*(n-j)/(j+1)
		sum+=p
	print(sum%1000000007)
	t-=1
