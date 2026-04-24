a=int(input())
b=[int(x) for x in input().split(" ")]
if a == len(b):
	print(sum(b[0:a:3]), sum(b[1:a:3]),sum(b[2:a:3]))
