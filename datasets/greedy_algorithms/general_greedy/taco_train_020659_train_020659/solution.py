t=int(input())
for i in range(t):
	N,M = list(map(int,input().split()))
	G = []
	P = []
	for i in range(N):
		g,p= list(map(int,input().split()))
		G.append(g)
		P.append(p)
	Pmin = min(P)
	if M > Pmin:
		print("YES")
	else:
		print("NO")
