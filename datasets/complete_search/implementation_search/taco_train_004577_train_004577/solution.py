(j, n) = (0, int(input()))
s = [input() for i in range(n)]
while len(set((i[j] for i in s))) == 1:
	j += 1
print(j)
