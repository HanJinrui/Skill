(n, m) = map(int, input().split())
arr = list(map(int, input().split()))

def work(sum, i, p):
	if i - 1 >= 0 and arr[i] != arr[i - 1]:
		sum += p * i * (n - i)
	if i + 1 < n and arr[i + 1] != arr[i]:
		sum += p * (i + 1) * (n - i - 1)
	return sum
sum = n * (n + 1) // 2
res = []
for i in range(1, n):
	if arr[i] != arr[i - 1]:
		sum += i * (n - i)
for w in range(m):
	(i, x) = map(int, input().split())
	i -= 1
	sum = work(sum, i, -1)
	arr[i] = x
	sum = work(sum, i, 1)
	res.append(sum)
print(*res, sep='\n')
