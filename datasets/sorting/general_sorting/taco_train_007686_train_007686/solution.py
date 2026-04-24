def binary_search(a, key, imin=0, imax=None):
	if imax is None:
		# if max amount not set, get the total
		imax = len(a) - 1

	while imin <= imax:
		# calculate the midpoint
		mid = (imin + imax)//2
		midval = a[mid]

		# determine which subarray to search
		if midval < key:
			# change min index to search upper subarray
			imin = mid + 1
		elif midval > key:
			# change max index to search lower subarray
			imax = mid - 1
		else:
			# return index number 
			return mid
	return imin   

def predecessor(a,x):
	m=binary_search(a,x)
	j=False
	while not j and m>0 and m<len(a)-1:
		if a[m-1]<a[m]:
			j=True
		m-=1
	return m

def sucessor(a,x):
	global n
	m=binary_search(a,x)
	if m>=n:
		return n
	if x!=a[m]:
		m-=1
	#print "m",m
	j=False
	while not j and m>=0 and m<len(a)-1:
		if a[m+1]>a[m]:
			j=True
		m+=1
	return m
#a=[4,4,4,4,4,5,6,8,9]
#print predecessor(a,8)
#print sucessor(a,4)
n=int(input())
k=list(map(int,input().split()))
#k=[i for i in xrange(1,101)]
k.sort()
#print len(k),k
q=int(input())
pred={}
succ={}
while q!=0:
	a,b=list(map(int,input().split()))
	if a not in pred:
	 x=predecessor(k,a)
	#print x
	
	 if x<n:
	  if k[x]>=a:
		x=x
	  else:
		x+=1    
	 pred[a]=x
	if b not in succ:  
	 y=sucessor(k,b)
	 if y<n:
		if k[y]>b:
			y-=1
	 succ[b]=y       
	#j==x and l==y
	j=pred[a]
	l=succ[b]        
	if j>=n and l>=n:
		print(0)
	elif j<n and l>=n: 
		l=n-1           
		print(abs(l-j)+1)
	else:
		print(abs(l-j)+1)    
	q-=1
