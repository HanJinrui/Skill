t = input()
r = r1 = ''
mx = -1
for i in range(len(t)):
	if t[i] >= 'A' and t[i] <= 'Z':
		r = r1 + '9'
		r1 = ''
	else:
		r = r + t[i]
		r1 = r1 + t[i]
	if int(r) > mx:
		mx = int(r)
print(mx)
