(n, m) = map(int, input().split())
fib = [1, 1]
for i in range(max(n, m)):
	fib.append(fib[-1] + fib[-2])
print(2 * (fib[n] + fib[m] - 1) % 1000000007)
