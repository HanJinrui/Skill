n = int(input())
arr = list(map(int, input().split()))
r = 0
for i in range(n):
	j = i
	while j + 1 < n and arr[j + 1] >= arr[j]:
		j += 1
	while j + 1 < n and arr[j] >= arr[j + 1]:
		j += 1
	r = max(r, j - i + 1)
print(r)
