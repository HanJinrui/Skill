t= int(input())
a=[]
for sfdgsdg in range(t):
	try:
		a.append(int(input()))
	except:
		a.appen

mn=min(10**7,max(a))
try:
	dp=[0]*(mn+1)
except:
	dp=[100000000]
dp[0]=0
dp[1]=0
dp[2]=1
dp[3]=1
def dynamic(n):
	for i in range(4,n+1):
		a = 1+dp[i/2] if i%2==0 else 10**9
		b= 1+dp[i-1]
		c= 1+dp[i/3] if i%3==0 else 10**9
		dp[i]=min(a,b,c)
		
dynamic(mn)

def solution(dp,i,depth=0):
	if i<10**7:
		return dp[i]
	if depth>13:
		return 10**9
	a = 1+solution(dp,i/2,depth+1) if i%2==0 else 10**9
	b= 1+solution(dp,i-1,depth+1)
	c= 1+solution(dp,i/3,depth+1) if i%3==0 else 10**9
	return min(a,b,c)
	
for i in a:
    print(solution(dp,i))
