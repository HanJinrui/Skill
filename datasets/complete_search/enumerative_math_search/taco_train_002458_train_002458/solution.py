n = int(input())
A = [*map(int, input().split())]
x = y = 0
for i in range(n):
	if A[i] == i:
		x += 1
	elif A[A[i]] == i:
		y = 1
print(x + y + (x != n))
