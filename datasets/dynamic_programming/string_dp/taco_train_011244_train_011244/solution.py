s = input()
for c in s:
	for i in range(len(s) + 1):
		f = s[:i] + c + s[i:]
		if f == f[::-1]:
			print(f)
			exit()
print('NA')
