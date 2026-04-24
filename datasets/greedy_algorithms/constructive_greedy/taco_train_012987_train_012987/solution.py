n = int(input())
s = input()
bal = 0
for c in s:
	if c == ')':
		bal -= 1
	print(bal & 1, end='')
	if c == '(':
		bal += 1
