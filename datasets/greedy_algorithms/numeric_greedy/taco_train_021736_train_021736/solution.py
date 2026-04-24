n = int(input())
A = list(map(int, input().split()))
print('1 1\n' + str(A[0] * (n - 1)))
if n < 2:
	print('1 1\n0')
else:
	print(2, n)
	print(*[(n - 1) * A[i] for i in range(1, n)])
print(1, n)
print(*[-n * A[i] for i in range(n)])
