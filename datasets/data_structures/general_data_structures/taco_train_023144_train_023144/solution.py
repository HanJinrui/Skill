def comp(p1,p2):
	if p1[0]==p2[0]:
		return p2[1]-p1[1]
	else:
		return p1[0]-p2[0]
t=eval(input())
while t:
	A=[]
	B=[]
	n=eval(input())
	for i in range(n):
		(a,b)=list(map(int,input().split()))
		A.append((a,b))
		B.append((a,0))
		B.append((b,1))
		i+=1
	B=sorted(B,cmp=comp)
	C=[0]*len(B)
	C[0]=1
	maxx=-float('inf')
	for i in range(1,len(B)):
		if B[i][1]==0:
			C[i]=C[i-1]+1
			maxx=max(maxx,C[i])
		else:
			C[i]=C[i-1]-1
	print(maxx)
	t-=1
