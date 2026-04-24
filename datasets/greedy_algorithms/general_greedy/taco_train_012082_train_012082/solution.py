t = int(input())
s = input()
c = 0
r = 0
for i in s:
	if i == '(':
		c += 1
	else:
		c += -1
		if c < 0:
			r += 2
if c != 0:
	print(-1)
else:
	print(r)
