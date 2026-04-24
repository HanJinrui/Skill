a=[]
for i in range(int(input())):
	k=int(input())
	if k:
		a.append(k)
	else:
		if len(a)>0:
			a.pop()
print(sum(a))
