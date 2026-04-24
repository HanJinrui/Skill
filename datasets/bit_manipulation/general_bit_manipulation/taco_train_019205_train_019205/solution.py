input()
xs = input().split()
for x in xs:
	if xs.count(x) == 1:
		print(x)
		break
