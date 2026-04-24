for _ in range(eval(input())):
	a,b = list(map(int,input().split()))
	if b==a+1:
		print(b&a)
	elif (b&1):
		print(b-1)
	else:
		print((b-2))
