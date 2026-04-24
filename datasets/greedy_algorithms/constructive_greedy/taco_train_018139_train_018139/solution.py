a = input()
print(*(int(x != y) for (x, y) in zip(a, a[1:] + 'b')))
