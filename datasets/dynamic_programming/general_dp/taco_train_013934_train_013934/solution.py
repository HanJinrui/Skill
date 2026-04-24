def d(x,y):
	return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
n=int(input())
l=[]
for i in range(n):
	i,j,k=list(map(int,input().split()))
	l.append((i,j,k))
dp=[-2494444444444]*(n+1)
#F=0
#L=n-1
dp[0]=l[0][2]
for i in range(1,n):
	for j in range(0,i):
		dp[i]=max(dp[i],dp[j]-d(l[i],l[j]))
	#print l[i][2]
	dp[i]+=l[i][2]
print("%.6f"%dp[n-1])
