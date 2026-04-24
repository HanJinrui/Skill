s = input()
a = -1
for i in range(1, len(s)):
	for j in range(i + 1, len(s)):
		x = [s[:i], s[i:j], s[j:]]
		if sum(map(lambda s: (len(s) < 2 or s[0] != '0') and int(s) <= 10 ** 6, [s[:i], s[i:j], s[j:]])) == 3:
			a = max(a, sum(map(int, x)))
print(a)
