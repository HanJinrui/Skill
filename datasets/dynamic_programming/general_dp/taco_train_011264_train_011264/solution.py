li=[0,1,2,4,7]
mod=1000000007
for _ in range(int(input())):
	m=int(input())
	while len(li)-1<m:
		li.append(sum(li[-3:])%mod)
	print((li[m]))
