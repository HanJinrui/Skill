from statistics import mode
for i in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	print(n - a.count(mode(a)))
