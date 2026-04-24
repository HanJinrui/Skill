t=int(input())
for x in range(t):
	a,b,c=0,0,0
	n=int(input())
	for x in range(n):
		shirt,pant,shoes=list(map(int,input().split()))
		x=min(b,c)+shirt
		y=min(a,c)+pant
		z=min(a,b)+shoes
		a,b,c=x,y,z
	print(min(a,b,c))
