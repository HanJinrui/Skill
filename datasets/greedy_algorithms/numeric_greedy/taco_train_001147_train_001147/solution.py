(y, k, n) = map(int, input().split())
print(*(range((k - y) % k or k, n - y + 1, k) or (-1,)))
