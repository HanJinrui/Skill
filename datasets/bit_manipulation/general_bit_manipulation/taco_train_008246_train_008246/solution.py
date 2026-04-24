def findp(arr , n):
	m = 10**9 + 7
	maximum = -1
	
	for i in range(1 , 1<<n):
		prod , s = 1 , 0
		for j in range(n):
			if i & (1<<j):
				s += arr[j]
				prod = (prod * arr[j]) % m
		maximum = max( ( prod * pow(s , m-2 , m) ) % m , maximum )
	return maximum 
 
t = int(input())
for k in range(t):
	#j = 1
	n = int(input())
	arr = list(map(int , input().split()))
	print("Case #%d: %d"%(k+1 , findp(arr , n)))
