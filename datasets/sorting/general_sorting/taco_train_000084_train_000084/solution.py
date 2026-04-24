arr = {(0,0)}

s = input()
l = len(s)
c=0

x,y = 0,0

for i in range(l):
	if s[i] == 'L':
		y = y-1
		
	elif s[i] == 'R':
		y = y+1

	elif s[i] == 'U':
		x = x-1

	elif s[i] == 'D':
		x = x+1
		
	arr.add((x,y))

c = l-len(arr)+1
print(c)
