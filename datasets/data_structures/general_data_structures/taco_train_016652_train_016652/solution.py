for _ in range(int(input())):
	a=input()
	n=int(input())
	hh=[]
	hhh=[]
	d=dict(list(zip(list(a),list(range(len(a))))))
	for i in range(n):
		z=input()
		h=[d.get(z[x]) for x in range(len(z))]
		hh.append(h)
		hhh.append((h,z))
	hhh.sort()
	
	jk=[y for (x,y) in hhh]
	for k in jk:
		print(k)
