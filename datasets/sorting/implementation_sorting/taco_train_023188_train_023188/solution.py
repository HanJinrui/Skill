for t in range(int(input())):
	n,k=list(map(int,input().split()))
	x=[]
	y=[0]*n
	for i in range(n):
		tmp=list(map(int,input().split()))
		x.append(sum(tmp))
		y=[a+b for a,b in zip(y,tmp)]
	xx=[0]*(k+1)
	yy=[0]*(k+1)
	for i in range(1,k+1):
		x_min=min(x)
		xx[i]=xx[i-1]+x_min
		x[x.index(x_min)]+=n
	for i in range(1,k+1):
		y_min=min(y)
		yy[i]=yy[i-1]+y_min
		y[y.index(y_min)]+=n
	ans=10**9
	for i in range(0,k+1):
		ans=min(ans,xx[i]+yy[k-i]+i*(k-i))
	print(ans)
