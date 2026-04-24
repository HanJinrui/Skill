t=int(input())
for _ in range(t):
	input()
	l=list(map(int,input().split()))
	print((' '.join(map(str,sorted(l,reverse=True)))))
