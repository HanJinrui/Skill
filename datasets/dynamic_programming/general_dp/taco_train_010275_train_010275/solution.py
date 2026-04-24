t = int(input())
import random
for ti in range(t):
	n,x = list(map(int,input().split()))
	a = [0 for _ in range(n)]
	a = list(map(int,input().split()))
	#a = sorted(a,reverse = True)
	for p in range(1000):
		t1,t2 = 0, 0
		aa = random.sample(a,n)
		i = 0
		ok = True
		while i<n:
			if t1<t2:
				t1 += aa[i]
			else:
				t2 += aa[i]
			i += 1
			if max(t1,t2)>x:
				ok = False
				break
		if ok:
			print("YES")
			break
	if not ok:
		print("NO")
