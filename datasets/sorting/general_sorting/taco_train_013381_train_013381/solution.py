for tc in range(eval(input())):
	n=eval(input())
	no=[0 for i in range(1002)]
	for i in input().split():
		no[int(i)]=1
	count=0
	i=1
	while i < 1001:
			count+=no[i]
			i+=(no[i] and no[i+1])+1
	print(count)
