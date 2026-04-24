l1=[]
for i in range(eval(input())):
	a=eval(input())
	l=[int(a) for a in input().split()]
	l1.append(set(l))
a=set().union(*l1)
b=set.intersection(*l1)
print((-sum(b)))
