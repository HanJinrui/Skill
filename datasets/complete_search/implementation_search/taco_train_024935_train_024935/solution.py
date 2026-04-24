n = int(input())
for i in range(n):
	(A, B, A1, B1, A2, B2) = map(int, input().split(' '))
	if {A, B} == {A1, B1}:
		print(1)
	elif {A, B} == {A2, B2}:
		print(2)
	else:
		print(0)
