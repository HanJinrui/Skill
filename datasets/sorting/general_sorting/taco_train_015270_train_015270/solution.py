cases=int(input())
flag=False;
flag2=False;





for i in range(cases):
	t=input().split()
	princes_cnt=int(t[0])
	hurdles_cnt=int(t[1])
	t=input().split()
	strengths=[int(x) for x in t]
	t=input().split()
	heights=[int(x) for x in t]
	h=0
	p=0

	
	for j in range(princes_cnt):
		
		strength=strengths[j]
	
		for k in range(h,hurdles_cnt):
			if(strength<heights[k]):
				break;
		if(k>h):
			h=k
			p=j
			
			
			
			
			
		
	print(p)
