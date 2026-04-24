T=eval(input())
lst=[0]*100100
lst[0]=1
lst[1]=1
lst[2]=2
lst[3]=4
I,mod =4,1000000007;
for I in range(4,100001):
	lst[I]=(lst[I-3]+lst[I-2]+lst[I-1])%mod;
while T >0:
	N=eval(input());
	print(lst[N]);
	T=T-1;
