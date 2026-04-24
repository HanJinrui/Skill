n = int(input())
r = sorted(zip(map(int, input().split()), map(int, input().split()), range(1, n + 1)))
print('%d\n%d' % (n // 2 + 1, r[n - 1][2]), end=' ')
for i in range(n - 2, 0, -2):
	print(r[i][1] < r[i - 1][1] and r[i - 1][2] or r[i][2], end=' ')
if ~n & 1:
	print(r[0][2])
