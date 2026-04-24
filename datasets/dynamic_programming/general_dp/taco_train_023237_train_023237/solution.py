MOD=1000000007
N,K=list(map(int,input().split()))
A=list(map(int,input().split()))
found=[0]*K
found[0]=1
Kplus=0
if sum(A)<2*K: 
	print(0)
	exit()
for a in A:
	Kplus=Kplus*2
	for j in range(max(0,K-a),K):
		Kplus+=found[j]
	Kplus%=MOD	
	for j in range(K-1,a-1,-1):
		found[j]=(found[j]+found[j-a])%MOD
print((MOD+Kplus-sum(found)%MOD)%MOD)
