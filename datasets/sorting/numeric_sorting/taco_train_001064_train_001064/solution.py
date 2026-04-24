mod = 998244353
n = int(input())
arr = [int(j) for j in input().split()]
fact = [1] * (3 * n)
for i in range(1, 3 * n):
	fact[i] = fact[i - 1] * i % mod
arr.sort()
print((sum(arr[n:]) - sum(arr[:n])) * fact[2 * n] * pow(fact[n], mod - 2, mod) ** 2 % mod)
