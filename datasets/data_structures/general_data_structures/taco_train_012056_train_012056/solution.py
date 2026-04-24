m,n=list(map(int,input().split()))
x=[int(i) for i in input().split()]
y=[int(i) for i in input().split()]
moves=0
for i in range(n):
	s1=abs(x[i]-1)+abs(y[i]-1)
	s2=abs(x[i]-m)+abs(y[i]-m)
	s3=abs(x[i]-1)+abs(y[i]-m)
	s4=abs(y[i]-1)+abs(x[i]-m)
	moves+=min(s1,s2,s3,s4)
print(moves)
