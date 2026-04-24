f = lambda q: 2 * min(t.count(q[0]), t.count(q[1]))
input()
t = input()
print(f('UD') + f('LR'))
