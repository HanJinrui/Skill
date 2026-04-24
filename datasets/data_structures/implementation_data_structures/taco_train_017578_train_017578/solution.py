input()
tmp = [int(i) for i in input().split()]
s = sum(tmp) / 2
j = 0
c = 0
for i in tmp[:-1]:
	j += i
	if j == s:
		c += 1
print(c)
