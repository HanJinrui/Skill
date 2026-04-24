a = int(input())
n = a
for i in range(2, n + 1):
	a = (a - 1) * i % 998244353
print(a)
