(X, Y, Z, N) = (int(input()) for _ in range(4))
print([[x, y, z] for x in range(X + 1) for y in range(Y + 1) for z in range(Z + 1) if x + y + z != N])
