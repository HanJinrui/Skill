n = int(input())
ar = input().strip().split()
ar = [int(e) for e in ar]
ma = 0
for i in range(n):
	j_1 = i
	j_2 = i
	while j_1 + 1 < n and ar[j_1 + 1] > ar[i]:
		j_1 += 1
	while j_2 - 1 >= 0 and ar[j_2 - 1] > ar[i]:
		j_2 -= 1
	c = ar[i] * (j_1 - j_2 + 1)
	if ma < c:
		ma = c
print(ma)
