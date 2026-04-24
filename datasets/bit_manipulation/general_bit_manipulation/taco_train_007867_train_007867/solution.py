t=0
for _ in range(int(input())):
	x,y=list(map(int,input().split()))
	t+=1
	c=0
	k=1
	while(True):
		if x+k==x^k:
			c+=1
		if c==y:
			break
		k+=1
	print("Case #%d:"%(t),k,end="")
	print("")
