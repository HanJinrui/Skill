def fun():
	s1 = input()
	s2 = input()
	for i in (s1[0], s2[0]):
		for j in (s1[1], s2[1]):
			for k in (s1[2], s2[2]):
				if i + j + k in {'bob', 'obb', 'bbo'}:
					return 'yes'
	return 'no'
T = int(input())
for i in range(T):
	print(fun())
