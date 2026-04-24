input()
xs = sorted((int(i) for i in input().split()))
result = min((j - i for (i, j) in zip(xs[:-1], xs[1:])))
print(result)
