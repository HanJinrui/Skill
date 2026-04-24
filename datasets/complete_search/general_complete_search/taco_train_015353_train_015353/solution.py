t = int(input())

for i in range(t):
	n,p = list(map(int, input().split()))
	while (n > 3 and p > 0) :
		n = n/2 + 1 if n%2 == 0 else n/2 +2
		p = p-1
	print(n)
