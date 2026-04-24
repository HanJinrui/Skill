I = lambda : map(int, input().split())
(*_, b) = I()
H = sorted(I())
print(H[b] - H[b - 1])
