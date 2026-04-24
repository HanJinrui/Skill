d = [0, 0, 0]
input()
for i in map(int, input().split()):
	d[i % 3] += 1
print(d[0] // 2 + min(d[1], d[2]))
