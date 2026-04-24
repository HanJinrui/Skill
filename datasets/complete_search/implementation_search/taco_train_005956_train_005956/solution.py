n = int(input())
arr = [0] + list(map(int, input().split())) + [0]
print(min((max(arr[i], arr[i + 1]) for i in range(n + 1))))
