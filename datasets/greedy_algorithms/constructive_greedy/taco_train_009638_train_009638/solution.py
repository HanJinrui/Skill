(n, a, b) = map(int, input().split())
if b == 0 and n > 1:
	if a == n - 1:
		print(-1)
		exit()
	print(1, end=' ')
	n -= 1
print(*[1 << i for i in range(b + 1)], end=' ')
print(*[(1 << b) + i + 1 for i in range(a)], end=' ')
print(*[1 for i in range(n - a - b - 1)], end=' ')
