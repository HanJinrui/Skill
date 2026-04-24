def sub(s, size):
	s1 = s[:size]
	s2 = s[size:]
	N = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
	for i in range(1, len(s1) + 1):
		for j in range(1, len(s2) + 1):
			if s1[i - 1] == s2[j - 1]:
				N[i][j] = N[i - 1][j] + N[i][j - 1] + 1
			else:
				N[i][j] = N[i - 1][j] + N[i][j - 1] - N[i - 1][j - 1]
	return N[-1][-1] - N[-2][-1]
num = int(input())
for n in range(num):
	inp = input()
	print(sum((sub(inp, i) for i in range(1, len(inp)))) % 1000000007)
