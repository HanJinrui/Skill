R = lambda : map(int, input().split())
input()
a = b = 0
for (x, y) in zip(R(), R()):
	(a, b) = (max(a, b + x), max(b, a + y))
print(max(a, b))
