a = int(input())
for i in range(a):
	c = int(input())
	b = list(map(int, input().split()))
	d = list(map(int, input().split()))
	d.sort()
	print(*d)
