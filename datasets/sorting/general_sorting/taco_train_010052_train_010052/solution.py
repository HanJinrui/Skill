import collections
for i in range(eval(input())):
	n=eval(input())
	a=list(map(int,input().split()))
	counter=collections.Counter(a)
	c=0
	for i in counter:
		c+= (counter[i]*(counter[i]+1))/2
	print(c)
