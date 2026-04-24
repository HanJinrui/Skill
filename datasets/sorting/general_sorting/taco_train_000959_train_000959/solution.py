t=eval(input())
while(t):
	n,q=list(map(int,input().split()))
	ran=[]
	l=[]
	for i in range(n):
		l=list(map(int,input().split()))
		ran.append(l)
	ran.sort()
	a=[0]
	b=[0]
	a[0]=ran[0][0]
	b[0]=ran[0][1]
	k=0
	for i in range(1,n):
		if ran[i][0]>b[k]:
			k+=1
			a.append(ran[i][0])
			b.append(ran[i][1])
		else:
			b[k]=max(b[k],ran[i][1])
	for i in range(q):
		c=0
		x=eval(input())
		flag=False
		tot=x
		for j in range(len(a)):
			temp=b[j]-a[j]+1
			if temp<tot:
				tot-=temp
			else:
				ans=a[j]+tot-1
				flag=True
				break
		if not flag:
			ans=-1
		print(ans)
	t-=1
