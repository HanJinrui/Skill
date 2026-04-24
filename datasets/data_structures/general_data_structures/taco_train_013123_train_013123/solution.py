l = []
for i in range(int(input())):
	inp = [int(x) for x in input().split()]
	if inp[0] == 1:
		l.append(inp[1])
	elif inp[0] == 2:
		l.pop(0)
	else:
		print(l[0])
