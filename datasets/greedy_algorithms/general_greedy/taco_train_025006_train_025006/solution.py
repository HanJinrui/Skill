s = input()
t = input()
m = 0
c = ''
for i in range(len(s)):
	if s[i] != t[i]:
		m ^= 1
		c += t[i] if m else s[i]
	else:
		c += s[i]
if m:
	print('impossible')
else:
	print(c)
