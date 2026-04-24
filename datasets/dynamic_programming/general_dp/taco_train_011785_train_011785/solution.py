T = int(input())
for j in range(T):
	N = int(input())
	a = list(map(int, input().split()))
	max1 = a[:]
	max2 = a[:]
	min1 = a[:]
	min2 = a[:]
	t = 0
	for i in range(1, N):
		max1[i] = max(max1[i - 1] + a[i], a[i])
		min1[i] = min(min1[i - 1] + a[i], a[i])
	for i in range(N - 2, -1, -1):
		max2[i] = max(max2[i + 1] + a[i], a[i])
		min2[i] = min(min2[i + 1] + a[i], a[i])
	for i in range(N - 1):
		t = max(t, abs(min1[i] - max2[i + 1]))
		t = max(t, abs(max1[i] - min2[i + 1]))
	print(t)
