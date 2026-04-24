n = int(input())
(x1, x2) = map(int, input().split())
arr = []
for i in range(n):
	(a, b) = map(int, input().split())
	arr.append([a * x1 + b, a * x2 + b])
arr.sort()
x = [i[1] for i in arr]
if sorted(x) == x:
	print('NO')
else:
	print('YES')
