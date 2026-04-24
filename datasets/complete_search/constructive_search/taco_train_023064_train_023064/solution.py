t = int(input())
for q in range(t):
	s = input()
	for i in range(1, len(s) - 1):
		if s[:i] <= s[i] >= s[i + 1:] or s[:i] >= s[i] <= s[i + 1:]:
			print(s[:i], s[i], s[i + 1:])
			break
