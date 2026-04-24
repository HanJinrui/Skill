MOD=1000000007
n,k =list(map(int, input().split()))

c=[]
for i in range(n):
	c.append(input().split())
s=input()
def choose(l,chosen):
	cnt=0
	if l==k: return 1
	for i in range(n):
		if not (chosen & (1<<i)):
			chosen |=1<<i
			fac=0
			for x in c[i]:
			    if x==s[l]: fac+=1
			if fac:
				cnt+=fac*choose(l+1,chosen)
			chosen -=1<<i
	return cnt                
chosen=choose(0,0)                 
print(chosen %MOD)
