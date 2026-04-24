n = int(input())
a = list(map(int, input().split()))
c = [n] * 100001
for i in range(n):
	c[a[i] - min(i, n - i - 1)] -= 1
print(min(c[1:]))
