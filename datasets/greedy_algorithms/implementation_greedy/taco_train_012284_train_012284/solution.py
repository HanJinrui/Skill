input()
t = {0}
i = s = 0
r = [0]
for x in map(int, input().split()):
	if (x > 0) & (x in t) | (x < 0) ^ (-abs(x) in t):
		r = (-1,)
		break
	if x > 0:
		t |= {x, -x}
	else:
		t -= {x}
	i += 1
	s += x
	if s == 0:
		r[0] += 1
		r += (i,)
		t = {0}
		i = 0
if s:
	r = (-1,)
print(r[0])
print(*r[1:])
