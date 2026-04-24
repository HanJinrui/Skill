q = int(input())
s1 = ''
s2 = []
for i in range(q):
	n = list(input().split())
	x = int(n[0])
	if x == 1:
		s2.append(s1)
		s1 += n[1]
	elif x == 2:
		s2.append(s1)
		s1 = s1[0:len(s1) - int(n[1])]
	elif x == 3:
		print(s1[int(n[1]) - 1])
	else:
		s1 = s2.pop()
