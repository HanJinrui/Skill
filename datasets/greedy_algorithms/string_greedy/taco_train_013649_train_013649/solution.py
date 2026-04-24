(n, pos) = (input(), -1)
for i in range(len(n) - 1):
	if n[i] in '02468':
		pos = i
		if n[i] < n[-1]:
			break
print(-1 if pos < 0 else n[:pos] + n[-1] + n[pos + 1:-1] + n[pos])
