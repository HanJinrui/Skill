T = int(input())
mod = 1000000007
for t in range(T):

	n = int(input())

	a = list(map(int,input().split()))

	a = sorted(a)

	i = 0
	ans = 1
	for x in a :
		ans = ans * max(0,x-i) %mod
		i += 1

	print(ans)
