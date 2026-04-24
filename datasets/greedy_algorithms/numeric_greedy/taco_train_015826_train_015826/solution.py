(a, n) = ([], input())
for i in [int(x) & 1 for x in input().split()]:
	if a and a[-1] == i:
		a.pop()
	else:
		a.append(i)
print(len(a) > 1 and 'NO' or 'YES')
