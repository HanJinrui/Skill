n=eval(input())
while n:
	p=eval(input())
	i=0
	j=2*p-1
	l=list(map(int, input().split()))
	l.sort()
	A=[]
	while i<j:
		A.append(l[i]+l[j])
		i+=1
		j-=1
	print(max(A))
	n-=1
