import collections
input()
a = collections.Counter(map(int, input().split()))
input()
b = collections.Counter(map(int, input().split()))
print(*sorted(b - a))
