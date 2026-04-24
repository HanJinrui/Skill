x = input().split()
n = int(x[0])
k = int(x[1])
A = list(map(int, input().split()))
A.sort()
ans = 0
n2 = n
for i in range(0, n2 // 2):
	if k > n - k:
		ans += (A[n2 - 1 - i] - A[i]) * (n - k)
		k -= 2
		n -= 2
	else:
		ans += (A[n2 - 1 - i] - A[i]) * k
		n -= 2
print(ans)
