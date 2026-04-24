n=eval(input())
m1=0
m2=0
l2=0
for i in range(n):
	a=input().strip()
	j=0
	l1=0
	while(j<1440):
		if a[j]=='C':
			while(j<1440 and a[j]=='C'):
				l2=l2+1
				l1=l1+1
				j=j+1
			if m1<l1:
				m1=l1
			l1=0
		else:
			j=j+1
			if m2<l2:
				m2=l2
			l2=0
	if l2>m2:
		m2=l2
print(m1,m2)
