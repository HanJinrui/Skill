T=int(input())
arr=list(map(int,input().strip().split(" ")))
arr.sort()
i=0
j=len(arr)-1
sum1=0
count=0
while i<j:
	sum1+=arr[j]-arr[i]
	count+=1
	if count%2==1:
		i+=1
	else:
		j-=1
sum2=0
count=0
i,j=0,len(arr)-1
while i<j:
	sum2+=arr[j]-arr[i]
	count+=1

	if count%2==1:
		j-=1
	else:
		i+=1
if sum2<sum1:
	print(sum1)
else:
	print(sum2)
