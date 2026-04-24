s = input()
l = input().split()
e = l[-1]
for i in range(len(l) - 2, -1, -1):
	if l[i] < e:
		break
	l[i + 1] = l[i]
	print(' '.join(l))
l[i + 1 if l[i] < e else i] = e
print(' '.join(l))
