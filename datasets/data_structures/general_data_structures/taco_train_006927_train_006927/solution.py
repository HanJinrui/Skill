a=[]
for i in range(int(input())):
	m=list(map(int,input().split()))
	if(m[0]==1):
		if(len(a)==0):
			print("No Food")
		else:
			print(a.pop())
	else:
		a.append(m[1])
