from queue import PriorityQueue
t = int(input())
for _ in range(t):
	n = int(input())
	L = list(map(int, input().split()))
	Q = PriorityQueue()
	for i in range(n):
		Q.put(L[i])
	ans = 0
	for i in range(n - 1):
		a = Q.get()
		b = Q.get()
		ans += a
		ans += b
		ans -= 1
		c = a + b
		Q.put(c)
	print(ans)
