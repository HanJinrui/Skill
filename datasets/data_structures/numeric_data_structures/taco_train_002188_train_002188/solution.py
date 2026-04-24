(c, y) = map(int, input().split())
x = list(map(int, input().split()))
if y == 0:
	y = 0
else:
	y = 1 if y % 2 else 2
for _ in range(y):
	a = max(x)
	x = [a - i for i in x]
print(*x)
