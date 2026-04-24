(n, m) = map(int, input().split())
coin = [int(x) for x in input().split()]
li = [0] * (n + 1)
li[0] = 1
for c in coin:
	for i in range(c, n + 1):
		li[i] += li[i - c]
print(li[n])
