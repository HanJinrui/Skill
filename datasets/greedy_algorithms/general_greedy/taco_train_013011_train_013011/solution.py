for tc in range(eval(input())):
	n=eval(input())
	b,g=tuple(map(int,input().split()))
	if abs(b-g)>1:
		print('Little Jhool wins!')
	else:
		print('The teacher wins!')
