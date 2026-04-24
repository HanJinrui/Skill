T=int(input())
for x in range(T):
	p,m=list(map(int,input().split(' ')))
	print((bin(p^m).count("1")))
