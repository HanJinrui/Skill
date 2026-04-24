x=eval(input())
a=[]
y=list(map(int,input().split()))
print("-1")
print("-1")
a.append(y[0])
a.append(y[1])
for i in range(2,x):
	a.append(y[i])
	a.sort()
	if(len(a)>3):
		a.pop(0)
	print(a[0]*a[1]*a[2])
