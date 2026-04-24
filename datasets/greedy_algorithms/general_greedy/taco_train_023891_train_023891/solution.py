n = int(input())
(a, b) = (list(map(int, input().split())), list(map(int, input().split())))
i = j = 0
while i < n and j < n:
	if b[j] == a[i]:
		i += 1
	j += 1
print(n - i)
