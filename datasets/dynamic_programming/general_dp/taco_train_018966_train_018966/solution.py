dis = list(range(1000000))
dis[0] = 1
dis[1] = 2
dis[2] = 4
for i in range(3 , 1000000):
	dis[i] = (dis[i-1] + dis[i-2] + dis[i-3])%1000000007	
	
t = int(input())
for _ in range(0,t):
	p = int(input())
	print(dis[p-1])
