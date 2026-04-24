#man u
t=eval(input())
for i in range(t):
	n,curr=list(map(int,input().split()))
	prev=None
	for j in range(n):
		pas=input()
		if pas[0]=="P":
				prev=curr
				curr=int(pas[2:])
		else:
				curr,prev=prev,curr
	print("Player",curr)
