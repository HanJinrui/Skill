n,m = list(map(int,input().split()))
A =  list(map(int,input().split()))
B =  list(map(int,input().split()))
for i in range(m):
	x,l,r=  list(map(int,input().split()))
	if x==1:
		print(sum(A[l-1:r:2]+B[l:r:2]))
	else:
		print(sum(B[l-1:r:2]+A[l:r:2]))
