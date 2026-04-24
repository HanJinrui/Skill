a = input()
s = ''
t = 0
for i in a:
	if i != 'a' and t != -1:
		s += chr(ord(i) - 1)
		t += 1
	else:
		s += i
		if t > 0:
			t = -1
if t == 0:
	s = s[:-1] + 'z'
print(s)
