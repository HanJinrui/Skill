t = int(input())
for i in range(t):
	(n, k) = map(int, input().split())
	a = sorted(map(int, input().split()))
	b = sorted(map(int, input().split()))
	print('YES' if all((a[i] + b[n - i - 1] >= k for i in range(n))) else 'NO')
