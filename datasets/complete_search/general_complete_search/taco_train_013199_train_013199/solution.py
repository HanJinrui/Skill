(a, p) = map(int, input().split())
print(sum([int(x + x[::-1]) for x in map(str, range(a + 1))]) % p)
