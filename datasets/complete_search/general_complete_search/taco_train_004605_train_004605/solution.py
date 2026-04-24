s=input()
sub=[]
n=len(s)
for i in range(0,n):
	for j in range(i,n):
		sub.append(s[i:j+1])
l=set(sub)

print(len(l))
