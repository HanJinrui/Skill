a = input()
for i in range(26):
	for j in range(len(a) + 1):
		b = a[:j] + chr(97 + i) + a[j:]
		if b == b[::-1]:
			print(b)
			exit()
print('NA')
