t= eval(input())
x=[]
while t:
	t-=1
	s=input()
	x.append(s)
b=[]
b=list(set(x))
b.sort()
for a in b:
	print(a,x.count(a))
