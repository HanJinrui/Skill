t = int(input())
for _ in range(t):
	(n, k) = map(int, input().split())
	arr = list(map(int, input().split()))
	if arr.count(0) == n:
		print(0)
		continue
	while arr.count(0) != 0 and k != 0:
		arr = [arr[i] + bool(arr[(i + 1) % n]) + bool(arr[(i - 1) % n]) for i in range(n)]
		k -= 1
	answer = sum(arr)
	answer += 2 * n * k
	print(answer)
