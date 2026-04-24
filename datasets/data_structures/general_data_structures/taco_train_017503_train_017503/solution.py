n = int(input())
c = [-1] * n + [0] * n
for (i, a) in enumerate(map(int, input().split())):
	c[i + max(0, n - a)] += 1
for i in range(2 * n - 2, -1, -1):
	c[i] += c[i + 1]
print(1 + max(range(n), key=lambda x: c[x] + c[x + n]))
