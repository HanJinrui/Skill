t=eval(input())
while t>0:
	a=list(input())
	b=list()
	while len(a):
		if len(a)%2!=0:
			b.append(a.pop(len(a)/2))
		elif a[len(a)/2]<a[(len(a)/2)-1]:
			b.append(a.pop(len(a)/2))
		else:
			b.append(a.pop(len(a)/2-1))
	b="".join(b)
	print(b)
	t=t-1
