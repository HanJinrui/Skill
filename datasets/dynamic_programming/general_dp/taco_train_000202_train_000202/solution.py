n=eval(input())
y=list(map(int,input().split()))
d={}
d[0]=1
for i in range(1,n):
	d[i]=1
	for j in range(i-1,-1,-1):
		if d[j]+1>d[i] and abs(y[j])<abs(y[i]) and y[j]*y[i]<0:
			d[i]=d[j]+1
print(max(d.values()))
