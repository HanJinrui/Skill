(ar, al) = map(int, input().split())
(br, bl) = map(int, input().split())
print('YES' if 2 * (ar + 1) >= bl >= ar - 1 or 2 * (al + 1) >= br >= al - 1 else 'NO')
