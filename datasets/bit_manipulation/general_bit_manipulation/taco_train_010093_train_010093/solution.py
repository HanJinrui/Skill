from itertools import combinations, chain
allsubsets = lambda n: list(chain(*[combinations(list(range(n)), ni) for ni in range(n+1)]))
t=int(input())
while t:
	hash=[0]*(2**15)
	n,p=list(map(int,input().split()))
	sub=allsubsets(n)
	ans=0
	while p:
		a,b=list(map(int,input().split()))
		for i in range(len(sub)):
			x=sub[i]
			if a-1 in x and b-1 in x and hash[i]==0:
				hash[i]=1
				ans+=1
		p-=1
	print((2**n)-ans-1)
	t-=1
