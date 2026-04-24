import itertools

def valid(m,S):
	W = []
	for k in S:
		if (m >= k):
			m -= k
			W.append(k)
	return (m==0,W)


def solve():
	
	m,n,N = list(map(int,input().split()))
	S = list(map(int,input().split())); S.sort(); S.reverse()
	T = list(map(int,input().split()))
	
	val = -1
	
	for r in range(len(T)):
		for z in itertools.combinations(T,r):
			p = sum(z)
			
			M = m - p
			q = valid(M,S)
			if (q[0]):
				val = max(val,M)
	if (val < 0):
		print("NO")
	else:
		print("YES")
		L = valid(val,S)[1]; L.sort()
		for k in L:
			print(k, end=' ')
		print()
			
					

t = eval(input())
for i in range(t):
	solve()
