for i in range(int(input())):
	n = int(input())
	a = input().split()
	b = []
	for i in a:
		b.append(a.count(i))
	print(n - max(b))
