input()
d = {(0, 0): 1}
r = s = i = 0
for x in map(int, input().split()):
	s ^= x
	i ^= 1
	c = d.get((s, i), 0)
	r += c
	d[s, i] = c + 1
print(r)
