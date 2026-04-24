import collections
x=int(input())
c=list(map(int,input().split()))
i=list(map(int,input().split()))
c=collections.deque(c)
s=0
n=0
while n<x:
	s+=1
	r=c.popleft()
	if i[n]==r:
		n+=1
	else:
		c.append(r)
print(s)
