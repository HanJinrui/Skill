n = int(input())
k = int(input()) - 1
a = sorted(list((int(input()) for i in range(n))))
print(min((a[i] - a[i - k] for i in range(k, n))))
