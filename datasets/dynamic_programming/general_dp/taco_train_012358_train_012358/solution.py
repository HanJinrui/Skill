for i in range(eval(input())):
	eval(input())
	s=0
	for j in (list(map(int,input().split()))):
		s=s+j
		#print s
	if s%2==0:
		print("YES")
	else:
		print("NO")
