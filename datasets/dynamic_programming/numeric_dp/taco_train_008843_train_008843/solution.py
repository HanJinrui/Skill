l = [0, 1, 3]
for i in range(10 ** 6):
	l.append((l[-1] * 2 - l[-3]) % (10 ** 9 + 7))
print(l[int(input())])
