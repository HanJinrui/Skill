n = int(input().split()[0])
c = [0] * 1001
for _ in [0] * n:
	c[int(input())] += 1
print(n - sum((x % 2 for x in c)) // 2)
