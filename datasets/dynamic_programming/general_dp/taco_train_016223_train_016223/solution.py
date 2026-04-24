for _ in range(eval(input())):
	n=eval(input())
	l=[[] for i in range(n)]
	for i in range(n):
		l[i]=list(map(int,input().split()))
	
	l.sort()
	l.reverse()
	m=[]
	for i in l:
		m.append(i[1])
	for i in range(1,n):
		for j in range(i):
			if l[i][0]<l[j][0] and l[i][1]<l[j][1]:
				m[i]=max(m[i],m[j]+l[i][1])
	print(max(m))
