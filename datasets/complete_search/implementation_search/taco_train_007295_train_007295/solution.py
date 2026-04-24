(l, r, k) = map(int, input().split())
print(*([k ** _ for _ in range(64) if l <= k ** _ <= r] or [-1]))
