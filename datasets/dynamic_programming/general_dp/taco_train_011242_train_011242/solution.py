import math
for _ in range(int(input())):
	x=int(input())
	li=[]
	for i in range(2,int(math.sqrt(x))+1):
		for j in range(2,int(math.log(x)/math.log(i))+1):
			li.append(i**j)
	li.append(1)
	li=set(li)
	for i in li:
		if x-i in li:
			print("Yes")
			break;
	else:
		print("No")
