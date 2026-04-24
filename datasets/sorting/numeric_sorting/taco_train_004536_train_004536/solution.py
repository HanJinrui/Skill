m=(10**9)+7
for _ in range(eval(input())):
	n=eval(input())
	x=sorted(map(int,input().split()))
	p=n-1
	s=0
	for i in range(n-1,-1,-1):
	#	print x[i],p
		s+=p*x[i]
		p-=2
	print((s*x[n-1])%m)
