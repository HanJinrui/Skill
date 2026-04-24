I = input
n = int(I())
x = int(I())
print('YNEOS'[any(({x, 7 - x} & set(map(int, input().split())) for _ in range(n)))::2])
