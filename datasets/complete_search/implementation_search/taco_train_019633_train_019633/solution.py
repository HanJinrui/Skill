A = [input() for _ in range(4)]
print('YES' if any(((A[i][j:j + 2] + A[i + 1][j:j + 2]).count('#') != 2 for i in range(3) for j in range(3))) else 'NO')
