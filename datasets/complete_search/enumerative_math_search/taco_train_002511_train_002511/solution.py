(n, h) = map(int, input().split())
for i in range(h, n, -1):
	if all((i % j for j in range(2, min(int(i ** 0.5), n) + 1))):
		print(i)
		exit()
print(-1)
