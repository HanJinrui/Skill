sze = eval(input())
s = input()
b = [1,0]

for x in range(2,95):
	b.append((x*b[x-1] + pow(-1,x))%1000000007)
if sze == 1:
	print((1))
else:	
	print((b[sze]))
