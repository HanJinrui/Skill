s = input()
t = input()
ans = 0
for i in range(len(s)):
	for j in range(i, len(s) + 1):
		tmp = s[:i] + s[j:]
		pos = 0
		for e in tmp:
			if e == t[pos]:
				pos += 1
				if pos == len(t):
					ans = max(ans, j - i)
					break
print(ans)
