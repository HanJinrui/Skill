for x in range(1,eval(input())+1):
	n,p,u,r,s=list(map(int,input().split()))
	for _ in range(n):
		if p+r<=u:
			p=p+r
		elif p-s>0:
			p=p-s
		else:
			break
	print("Case #{0}: {1} ".format(x,p))
