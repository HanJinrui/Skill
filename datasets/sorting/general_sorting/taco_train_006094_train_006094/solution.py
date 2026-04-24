ceo,coo,cto=list(map(int,input().split()))
n=eval(input())
h=list(map(int,input().split()))
h.sort()
o=abs(min(coo,cto)-h[0])+abs(max(coo,cto)-h[n-1])
h.insert((n+1)/2,ceo)
for i in range(n):
	o+=abs(h[i+1]-h[i])
print(o)
