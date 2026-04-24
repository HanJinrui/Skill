(n, k) = [int(i) for i in input().split()]
c = sorted([int(i) for i in input().split()])[::-1]
res = 0
for b in range(n):
	res += c[b] * (b // k + 1)
print(res)
