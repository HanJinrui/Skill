N,M=list(map(int,input().strip().split()))
req={}
car=[0]*M
for i in range(1,N+1):
	S,J=list(map(int,input().strip().split()))
	req[S]=[i,J]
res=['-1']*N
k=list(req.keys())
k.sort()
for i in k:
	temp = req[i]
	for j in range(M):
		
		if i>=car[j]:
			car[j]=i+temp[1]
			res[temp[0]-1]=str(j+1)
			# print i,temp,car,res
			break
print(' '.join(res))
