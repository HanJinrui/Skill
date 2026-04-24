(n, m) = map(int, input().split())
s = input()
freq = [0] * 10
B = [0] * n
for i in range(0, n):
	t = int(s[i])
	freq[t] += 1
	for j in range(0, 10):
		B[i] += freq[j] * abs(t - j)
for i in range(0, m):
	x = int(input())
	print(B[x - 1])
