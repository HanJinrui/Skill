def jõuab(a, b):
	return a[0] - b[0] >= abs(a[1] - b[1]) + abs(a[2] - b[2])
a = [[[0, 1, 1]]]
b = int(input().strip().split(' ')[1])
for i in range(b):
	if a[-1] != []:
		a.append([])
	j = len(a) - 1
	c = list(map(int, input().strip().split(' ')))
	while j > 0:
		for k in a[j - 1]:
			if jõuab(c, k):
				a[j].append(c)
				j = 0
				break
		j -= 1
print(len(a) - 1) if a[-1] != [] else print(len(a) - 2)
