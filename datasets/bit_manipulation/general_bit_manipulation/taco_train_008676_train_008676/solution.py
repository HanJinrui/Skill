def cnt(x):
	res = 0
	while x:
		x = x & (x - 1)
		res += 1
	return res

for _ in range(eval(input())):
	n = eval(input())
	a = [cnt(x) for x in map(int, input().split())]
	print(min(a))
