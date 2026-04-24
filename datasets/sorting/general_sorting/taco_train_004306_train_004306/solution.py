n, q = [int(s) for s in input().split()]
arr = set([int(s) for s in input().split()])
for _ in range(q):
	print('YES' if eval(input()) in arr else 'NO')
