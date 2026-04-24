'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
#print 'Hello World!'
from fractions import gcd
t=eval(input())
while t>0:
	t-=1
	a,b,n=list(map(int,input().split()))
	c=(a*b)/(gcd(a,b))
	l,r=1,1000000000000
	while(l<=r):
		m=(l+r)/2
		s=m/a+m/b-m/c
		if (s==n):
			print(max((m/a)*a,(m/b)*b))
			break
		elif (s<n):
			l=m+1
		else:
			r=m-1
