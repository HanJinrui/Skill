arr=[6,2,5,5,4,5,6,3,7,6]
for _ in range(eval(input())):
	a=list(input())
	temp=0

	for item in a:
		temp=temp+arr[int(item)]
		
	print(temp)
