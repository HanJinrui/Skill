b = int(input().split()[1])
s = 0
for i in map(int, input().split()):
	i += s
	print(i // b)
	s = i % b
