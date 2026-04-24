import bisect;
n=eval(input());	A=list(map(int,input().split()));	V,su=[],0;
for i in A:	su+=i;	V.append(su);
for i in range(int(input())):
	z=int(input());	x=bisect.bisect_left(V,z);
	if x==n:	print(-1)
	else:	print(x+1)
