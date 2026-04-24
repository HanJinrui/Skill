x=eval(input())
for _ in range(0,x):
	y=eval(input())
	f=list(map(int,input().split()))
	mi=min(f)
	ma=max(f)
	k=1
	c=0
	gr=mi
	for i in f:
		if i !=0:
			k=k*i
			if i<0:
				c=c+1
				if i>gr:
					gr=i
	if k<mi:
		mi=k
	if gr!=0 and k/gr<0:
		mi=k/gr
	if c%2!=0:
		k=k/gr
	if c==1 and ma==0:
		k=0
	if ma==mi and ma==0:
		k=0


	if len(f)==1:
		print(f[0],f[0])
	else:
		print(k,mi)
