n=eval(input())
ans=0
l=sorted(map(int,input().split()))
for i in range(0,len(l)-2):
	a=abs(l[i]-l[i+1])
	b=abs(l[i]-l[i+2])
	c=max(a,b)
	if c>ans:
		ans=c
print(ans)
