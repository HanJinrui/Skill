n,q=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
c=[0]
i=0
while n>0:
	i=i+a[n-1]
	c.append(i)
	n=n-1
for _ in range(q):
	k=eval(input())
	print(c[k])
