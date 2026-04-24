input()
a = list(map(int, input().split()))
print([a.index(min(a)) + 1, 'Still Rozdil'][a.count(min(a)) > 1])
