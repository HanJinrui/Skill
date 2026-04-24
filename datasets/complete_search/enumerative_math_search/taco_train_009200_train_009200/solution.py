input()
a = (*map(int, input().split()),)
print(max(max((y - x for (x, y) in zip(a, a[1:]))), min((z - x for (x, _, z) in zip(a, a[1:], a[2:])))))
