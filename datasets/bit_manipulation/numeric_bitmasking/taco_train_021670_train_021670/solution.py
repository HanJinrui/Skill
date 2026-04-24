t = int(input())
for i in range(t):
	l = list(map(int, input().split()))
	t = 0
	for j in range(len(l)):
		if l[j] - 1 >= 0:
			l[j] = l[j] - 1
			t += 1
	l.sort()
	if l >= [2, 2, 2]:
		t += 3
	elif l >= [1, 1, 2]:
		t += 2
	elif l >= [0, 1, 1]:
		t += 1
	print(t)
