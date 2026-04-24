(n, t) = (int(input()), list(map(int, input().split())))
print(max((sum(t[j::i]) for i in range(1, n // 3 + 1) if n % i == 0 for j in range(i))))
