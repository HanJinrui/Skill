input()
t = list(map(int, input().split()))
for i in range(2, len(t)):
	if (t[i] - t[i - 1]) * (t[i - 1] - t[0]) < 0:
		print(3, 1, i, i + 1)
		exit()
print(0)
