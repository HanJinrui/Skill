input()
x = 0
for i in map(int, input().split()):
	x |= i
print(x)
