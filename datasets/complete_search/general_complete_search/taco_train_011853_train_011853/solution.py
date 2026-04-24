(n, _) = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr, reverse=True)
ans = [n]
for i in arr:
	while n % i == 0:
		ans.insert(0, n // i)
		n //= i
	if n == 1:
		print(' '.join(map(str, ans)))
		break
else:
	print(-1)
