n = int(input())
a = list(map(int, input().split()))
r = list(range(0, n))
z = sorted(zip(a, r))
m = 10 ** 16
for i in range(0, n - 1):
	if z[i][1] > z[i + 1][1]:
		m = min(z[i + 1][0] - z[i][0], m)
print(m)
