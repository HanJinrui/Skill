(n, k) = map(int, input().split())
l = input().split()
while n and l[n - 1] == l[-1]:
	n -= 1
print(n if k > n else -1)
