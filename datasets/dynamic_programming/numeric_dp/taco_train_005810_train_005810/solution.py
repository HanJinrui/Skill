for _ in range(eval(input())):
	a,b,c=list(map(int,input().split()))
	print("%.1f" %(float(min(a,b,c))/2))
