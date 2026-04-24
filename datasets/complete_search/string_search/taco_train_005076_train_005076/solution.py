for t in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	for i in range(n):
		p = input().split()
		a[i] = (a[i] + p[1].count('D') - p[1].count('U')) % 10
	print(*a)
