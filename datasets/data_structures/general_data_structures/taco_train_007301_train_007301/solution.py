n,x=list(map(int,input().split()))
a=[]
a=input().split()
skip=0
ans=0
for i in a:
	if skip<=1:
		if int(i)<=x:
			ans=ans+1
		else:
			skip=skip+1
print(ans)
