m =eval(input())
p =  eval(input())
arr = list(map(int,input().split()))
hi = sum(arr)
lo=0
while(hi>=lo):
	mid = (hi+lo)/2
 	s=0
 	c=0
 	for i in range(len(arr)):
 		s+=arr[i]
 		if s>mid:
 			c+=1
 			s=arr[i]
 			if s>mid:
 				c=-1
 				break
# 	print hi,lo,mid,c
 	if c==-1:
 		lo = mid+1
 	elif c<m:
 		hi = mid-1
 	else:
 		lo=mid+1
print(lo)
