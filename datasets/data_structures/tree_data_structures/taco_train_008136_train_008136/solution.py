mod = 10 ** 9 + 7
(N, K) = map(int, input().split())
print(pow(K * N, N - 2, mod) * pow(pow(N * K - K, K - 1, mod), N, mod) % mod if N != 1 else 1 if K == 1 else 0)
