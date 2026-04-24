N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
s = 0
M = 1000000007
for i in range(N):
	s += A[i] * (pow(2, N - i - 1, M) - pow(2, i, M))
	s %= M
print(s)
