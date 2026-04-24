input()
r = 1
for e in sorted(map(int, input().split())):
	r += e >= r
print(r)
