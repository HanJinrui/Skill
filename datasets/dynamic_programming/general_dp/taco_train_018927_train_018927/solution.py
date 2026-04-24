'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
#print 'Hello World!'
n= int(input());
s=[int(0)]*1000001;

for i in range(0,n):
	b,c=input().split();
	s[int(b)] = int(c);

m=int(input());
r=int(0);
for i in range(999999,-1,-1):
	s[i]=max(s[i],s[i+1]);
	
for i in range(0,m):
	num = int(input());
	r += int(s[num]/num);
				

	
print((r*100));
