for i in range(int(input())):
	x,y,n,w,per1,per2 = [int(x) for x in input().split(" ")]
	p1=per1*0.01
	p2=per2*0.01
	temp=[]
	for j in range(n+1):
		row=[]
		for k in range(w+1):
			if k==0:
				row.append(1)
			else:
				row.append(0)
		temp.append(row)
	for j in range(1,n+1):
		for k in range(1,w+1):
			temp[j][k]=max(p1*temp[j-1][max(0,k-x)]+(1-p1)*temp[j-1][max(0,k)],p2*temp[j-1][max(0,k-y)]+(1-p2)*temp[j-1][max(0,k)])
		
	print(('%0.6f' %(temp[n][w]*100)))
