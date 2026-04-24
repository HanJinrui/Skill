import math
t=eval(input())
#2n*(2n+2)+4n*n or 4n^2+8n+4
for i in range(t):
	n=eval(input())
	if n<12:
		print(0, end=' ')
		print(0)
		continue
	x=int((-4+math.sqrt(16+32*n))/16.0)
	xplus=int((-12+math.sqrt(16+32*n))/16.0)
	if 8*pow(x,2)+4*x>8*pow(xplus,2)+12*xplus+4:
		print(2*x-1, end=' ')
		print(2*x)
	else:
		print(2*xplus+1, end=' ')
		print(2*xplus)
'''8x^2+4x-n=0
x=(-4+sqrt(16+32n))/16.0
8x^2+12x-n+4=0
x=(-12+sqrt(16+32n))/16.0'''
