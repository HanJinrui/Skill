input()
l = sorted(map(int, input().split()))
print(max(0, len(l) - l.count(l[0]) - l.count(l[-1])))
