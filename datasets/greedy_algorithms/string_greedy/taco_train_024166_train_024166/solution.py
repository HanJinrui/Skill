s = input()
t = ''
c = ord('a')
for i in s:
	if ord(i) <= c <= ord('z'):
		t += chr(c)
		c += 1
	else:
		t += i
if c <= ord('z'):
	t = -1
print(t)
