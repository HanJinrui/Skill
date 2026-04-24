t=eval(input())
while t>0:
	a,b,c,k=list(map(int,input().split()))
	i=50
	while True:
		if (a*i*i)+(b*i)+(c)>=k:
			j=i-50
			while j<=i:
				if (a*j*j)+(b*j)+(c)>=k:
					print(j)
					break
				j+=1
			break
		i+=50
	t-=1
