(n, t) = (int(input()) - 1, sorted(list(map(int, input().split()))))
print('YNEOS'[all((2 * t[i] <= t[i + 1] for i in range(n) if t[i] < t[i + 1]))::2])
