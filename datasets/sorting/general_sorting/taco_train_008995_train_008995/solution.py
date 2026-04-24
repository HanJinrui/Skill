s = input()
l = [int(i) for i in input().split()]
for i in range(1, len(l)):
	for j in range(0, i):
		if l[i] < l[j]:
			(l[j], l[i]) = (l[i], l[j])
	print(' '.join([str(i) for i in l]))
