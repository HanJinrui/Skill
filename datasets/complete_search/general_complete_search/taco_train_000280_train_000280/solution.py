no=int(input(""))
l=list(map(int,input("").split()))
cnt=0
for i in l:
	cnt=0
	for j in l:
		if i%j==0:
			cnt+=1
	if cnt==1:
		print(i, end=' ')
