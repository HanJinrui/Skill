t=int(eval(input()))
for i in range(0,t):
	a,b,c=list(map(int,input().split()))
	ans=1
	p=a*b
	while(p<c):
		p*=a*b
	p/=a*b
	if p*a>=c or p*b>=c :
		print("Adam")
	else:
		print("Bob")
