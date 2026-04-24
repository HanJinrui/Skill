def check(a,x,k):
	prev_pos=x+a[0]
	k-=1
	i=1
	while i<len(a):
		next_pos=prev_pos+x
		if a[i]<=next_pos:
			i+=1
			continue
		prev_pos=a[i]+x
		i+=1
		k-=1
	return k>=0
n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
a=sorted(a)
l=0
r=10**7
ans=0
while l<=r:
	mid=r-(r-l)/2
	if check(a,mid,k):
		ans=mid
		r=mid-1
	else:
		l=mid+1
print(ans)
