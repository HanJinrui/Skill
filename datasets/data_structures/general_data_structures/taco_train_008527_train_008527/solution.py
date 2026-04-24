import heapq
m,n=list(map(int,input().split()))
a=[-int(x) for x in input().split()]
heapq.heapify(a)
s=0
for i in range(n):
	t=heapq.heappop(a)
	s+=-t
	t+=1
	if t<0:
		heapq.heappush(a,t)
print(s)
