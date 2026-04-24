n=input()
x=list(map(int,input().split()))
even=[]
odd=[]
for i in x:
	if i%2==0:
		even.append(i)
	else:
		odd.append(i)

print(' '.join(map(str,sorted(even))),sum(even), ' '.join(map(str,sorted(odd))),sum(odd))
