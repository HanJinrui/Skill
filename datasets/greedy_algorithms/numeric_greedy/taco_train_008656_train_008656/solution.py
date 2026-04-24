A = list(map(int, input().split()))
t = 0
while max(A) > 0:
	A[t % 3] -= 2
	t += 1
print(t + 29)
