n=int(input())
arr=list(map(int,input().split()))
look=[0]*(max(arr)+1)
look_count=[0]*(max(arr)+1)

for i in range(len(arr)):
	look_count[arr[i]]+=1

for i in range(len(arr)-1):
	if arr[i]==arr[i+1]:
		look[arr[i]]+=1
mx=max(look)
if max(look_count)>(n+1)/2:
	print(-1)
else:
	print(max(mx,(sum(look)+1)/2))
