n,p=list(map(int,input().split()))
p=p/100.0
dp=[-1]*(n+1)
dp[0]=1
dp[1]=0
dp[2]=p
dp[3]=1-p
for i in range(4,n+1):
	dp[i]=dp[i-2]*p+dp[i-3]*(1-p)
print("%.6f"%dp[n])
