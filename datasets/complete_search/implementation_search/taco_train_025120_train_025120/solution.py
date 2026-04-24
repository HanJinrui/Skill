(a, b) = input().split()
for i in range(max(int(a) + 1, int(b)), 999999):
	if ''.join((c for c in str(i) if c in '4,7')) == b:
		print(i)
		exit()
