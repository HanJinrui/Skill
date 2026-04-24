from heapq import *
l = input()
k = int(input())
n = len(l)
if k > n * (n + 1) / 2:
	print('No such line.')
	quit()
ss = [(l[i], i) for i in range(n)]
heapify(ss)
while k:
	k -= 1
	t = heappop(ss)
	if k == 0:
		print(t[0])
	elif t[1] < n - 1:
		heappush(ss, (t[0] + l[t[1] + 1], t[1] + 1))
