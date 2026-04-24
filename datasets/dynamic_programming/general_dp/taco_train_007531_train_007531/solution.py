arrR=list(map(int, input().split()))
N=int(input())

pr2=["02","03","05","07","11","13","17","19","23","29","31","37","41","43","47","53","59","61","67","71","73","79","83","89","97"]

if arrR[0]!=0:
	for i in range(N):
		print("0")
else:
	univ=[]
	possnums=[(i,False) for i in range(1,10)] # regarding modulo, all 1-digit nums are OK
	for i in range(2,16):
		nums=[]
		for num,bCont in possnums:
			for k in range(10):
				if (num*10+k)%i==arrR[i-1]:
					if bCont or str(num*10+k)[-2:] in pr2:
						nums.append((num*10+k,True))
						univ.append(num*10+k)
					else:
						nums.append((num*10+k,False))
		possnums=nums
	for i in range(N):
		A,B=list(map(int,input().split()))
		if A>univ[-1] or B<univ[0]:
			print(0)
		else:
			if A<=univ[0]:
				idxA=0
			else:
				left=0
				right=len(univ)-1
				while not left==right-1:
					mid=left+(right-left)/2
					if univ[mid]<A:
						left=mid
					else:
						right=mid
				idxA=right
			if B>=univ[-1]:
				idxB=len(univ)-1
			else:
				left=0
				right=len(univ)-1
				while not left==right-1:
					mid=left+(right-left)/2
					if univ[mid]<=B:
						left=mid
					else:
						right=mid
				idxB=left
			print(idxB-idxA+1)
