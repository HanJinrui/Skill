l=[ ]
for _ in range(eval(input())):
	l.append(input())
l.sort()
l2=len(l)
c=0
while c!=l2:
	l1=l.count(l[c])
	print("%s %d"%(l[c],l1))
	c+=l1
