(k, r, v, f) = sorted(map(int, input().split()))
x = min(f - r - v, v - k - r)
print(['SEGMENT', 'IMPOSSIBLE', 'TRIANGLE'][(x > 0) - (x < 0)])
