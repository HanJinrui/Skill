(n, x) = map(int, input().split())
d = []
for i in range(2 ** n):
	if i < i ^ x:
		d.append(i)
print(len(d) - 1)
for i in range(1, len(d)):
	print(d[i] ^ d[i - 1], end=' ')
