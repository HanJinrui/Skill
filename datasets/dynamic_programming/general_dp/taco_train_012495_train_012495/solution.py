T = int(input())

def run(x, y):
	if x * y == 0:
		return max(x, y)
	return (int(x / 2) + y) * 2 + x % 2
for _ in range(T):
	(x, y) = [int(x) for x in input().split()]
	print(run(x, y))
