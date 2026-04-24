n = int(input())
aa = list(map(int, input().split()))
live = []
ans = 0
for i in range(n - 1, -1, -1):
	c = 0
	while len(live) != 0 and live[-1][0] < aa[i]:
		c = max(c + 1, live[-1][1])
		live.pop()
	if c > ans:
		ans = c
	live.append((aa[i], c))
print(ans)
