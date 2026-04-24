n, k = list(map(int, input().split()))

li = [0] * (n+2)

i = 2
while i<=n:
	if li[i]==0:
		j = i
		while j<=n:
			li[j] += i
			j += i
	i += 1

print(li.count(k))
