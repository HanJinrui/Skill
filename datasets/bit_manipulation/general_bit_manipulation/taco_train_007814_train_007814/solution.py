T = int(input())
while T:
	flag=False
	N = int(input())
	arr = [int(i) for i in input().split()]
	ok=False
	for i in range(32):
		first=True
		mul=0
		for j in range(len(arr)):
			
			if 1&(arr[j]>>i):
				if first:
					mul = arr[j]
					first = False
				else:
					mul = mul & arr[j]
			if bin(mul).count('1')==1: 
				ok=True
	if ok:
		print("YES")
	else:
		print("NO")
 
	T -= 1
