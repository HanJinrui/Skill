'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
n=eval(input())
m=list(map(int,input().split()))
l=[]
for i in range(n):
	l.append(1)
for i in range(n):
	for j in range(i):
		if m[i]>m[j] and l[i]<l[j]+1:
							   l[i]=l[j]+1
							   
print(bin(max(l))[2:])
