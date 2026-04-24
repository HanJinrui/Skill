(n, w) = map(int, input().split())
l = sorted(map(int, input().split()))
print(min(w, l[n] * n * 1.5, l[0] * n * 3))
