t = int(input())
for i in range(t):
	N,K,M = list(map(int, input().strip().split(' ')))
	ip = []
	for i in range(N):
		ip.append(input())
	ip.sort()
	print(ip[K-1])
