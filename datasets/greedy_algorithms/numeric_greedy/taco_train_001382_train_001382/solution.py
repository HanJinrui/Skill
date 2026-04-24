test = int(input())
for t in range(test):
	n, m = list(map(int,input().split()))
	answer = 0
	while n>0:
		answer += n%m
		n = n/m
	print(answer)
