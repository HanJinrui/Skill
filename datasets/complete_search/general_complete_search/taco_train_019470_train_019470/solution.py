A = [list(map(int, input().split())) for _ in range(int(input()))]
print(sum((h < v for h in map(sum, A) for v in map(sum, zip(*A)))))
