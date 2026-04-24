for _ in range(eval(input())):
	a=[]
	n=eval(input())
	for i in range(n):
		a.append(list(map(int,input().split())))
	c=[]
	tmp=0
	for x,y in a:
		c.append(x+y)
		tmp+=y
	c.sort()
	print(sum(c[-2:])-tmp)
