def do_task(a,x,y):
	for i in range(0,x+1):
		for j in range(0,y+1):
			if a[i][j] == 1:a[i][j] = 0
			else:a[i][j] = 1
	return a
	
t = eval(input())	
while t:
	n,m = list(map(int,input().split(' ')))
	row = n - 1
	col = m - 1
	a = []
	while n:
		a.append(list(map(int,list(input()))))
		n -= 1
	
	c = 0
	for i in range(row,-1,-1):
		for j in range(col,-1,-1):
			if a[i][j] == 0:
				a = do_task(a,i,j)
				c += 1
	
	print(c)
	
	t -= 1
